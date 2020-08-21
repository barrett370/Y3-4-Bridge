## Selenium Tests

from django.contrib.auth.models import User
from blog.models import Post
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
