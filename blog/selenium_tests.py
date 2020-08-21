## Selenium Tests

from django.contrib.auth.models import User
from blog.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from django.db.utils import IntegrityError
import pytz


class BlogFunctionalTest(StaticLiveServerTestCase):
    test_post_id: str = "46c3c3c7-d1c2-4649-aae9-f3f79ace13ba"  # example uuid4 id
    test_title = "Test Post #1"
    test_text = "test text"
    test_create_date = datetime.fromtimestamp(1326244364, tz=pytz.UTC)
    test_publish_date = datetime.fromtimestamp(1326244375, tz=pytz.UTC)

    test_skill_id = "0e538346-0474-4ee0-8f7f-c47f2568b6ee"
    test_skill_title = "Test Skill"
    test_skill_desc = "This is a test skill for functional tests"
    test_skill_exp = "1s"

    test_uni_course_id = "dbe21966-5b8a-442c-8f70-0f840fd12ae5"
    test_uni_course_title = "Test University Course"
    test_uni_course_description = (
        "This is a test course for functional testing purposes"
    )
    test_uni_course_completion_date = datetime.fromtimestamp(
        1326244375, tz=pytz.UTC
    ).date()
    test_uni_course_grade = "70%"
    test_uni_course_level = "university"

    test_misc_course_id = "89a6e329-4d21-41fe-9688-a3f259bd9dce"
    test_misc_course_title = "Test Misc Course"
    test_misc_course_description = (
        "This is a test course for functional testing purposes"
    )
    test_misc_course_completion_date = datetime.fromtimestamp(
        1326244375, tz=pytz.UTC
    ).date()
    test_misc_course_grade = "70%"
    test_misc_course_level = "other"

    test_cv_phone_number = "12345678901"
    test_cv_email_address = "foo@bar.baz"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def create_test_post(self):
        try:
            self.user = User.objects.create_user(
                username="test_user", email="", password="Passw0rd"
            )
        except IntegrityError:
            pass

        Post.objects.create(
            post_id=self.test_post_id,
            author=self.user,
            title=self.test_title,
            text=self.test_text,
            created_date=self.test_create_date,
            publish_date=self.test_publish_date,
        )

    def test_post_list(self):
        self.create_test_post()
        self.driver.get(self.live_server_url)
        post = self.driver.find_elements_by_class_name("post")
        self.assertEqual(self.driver.title, "Sam Barrett Bridging coursework Blog")
        self.assertNotEqual(post, [])

    def test_post(self):
        self.create_test_post()
        self.driver.get(self.live_server_url + "/post/" + self.test_post_id)
        self.assertEqual(self.driver.title, "Sam Barrett Bridging coursework Blog")
        post_title = self.driver.find_element_by_id("post_title")
        self.assertEqual(post_title.text, self.test_title)
        post_text = self.driver.find_element_by_id("post_text")
        self.assertEqual(post_text.text, self.test_text)

    def create_test_cv(self):

        # create test tech skill
        TechSkill.objects.create(
            skill_id=self.test_skill_id,
            title=self.test_skill_title,
            description=self.test_skill_desc,
            experience_amount=self.test_skill_exp,
        )

        # Create a test univeristy module
        Course.objects.create(
            course_id=self.test_uni_course_id,
            title=self.test_uni_course_title,
            description=self.test_uni_course_description,
            completion_date=self.test_uni_course_completion_date,
            grade=self.test_uni_course_grade,
            course_level=self.test_uni_course_level,
        )

        # Create a test misc module
        Course.objects.create(
            course_id=self.test_misc_course_id,
            title=self.test_misc_course_title,
            description=self.test_misc_course_description,
            completion_date=self.test_misc_course_completion_date,
            grade=self.test_misc_course_grade,
            course_level=self.test_misc_course_level,
        )

        # Create test cv
        CV.objects.create(
            phone_number=self.test_cv_phone_number,
            email_address=self.test_cv_email_address,
        )

    def test_cv(self):
        self.create_test_cv()
        self.driver.get(self.live_server_url + "/cv")
        expected_cv = open("expected_pages/expected_cv.html", "r").read()

        # f = open("exception_cv.html", "w")
        # f.write(self.driver.page_source)
        # f.close()
        self.assertEqual(self.driver.page_source, expected_cv)

    def test_navigation_bar(self):
        self.create_test_cv()
        body = self.driver.find_element_by_tag_name("body")
        print(body.text)
        nav_bar = body.find_element_by_id("nav-bar")
        nav_bar.find_element_by_link_text("Home").click()

        expected_cv = open("expected_pages/expected_cv.html", "r").read()

        self.assertEqual(self.driver.page_source, expected_cv)
        self.create_test_post()
        self.driver.find_element_by_link_text("My CV").click()

