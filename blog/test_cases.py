from django.test import TestCase
from blog.models import Post
from datetime import datetime
from django.contrib.auth.models import User
import pytz


class PostTest(TestCase):
    test_post_id: str = "46c3c3c7-d1c2-4649-aae9-f3f79ace13ba"  # example uuid4 id
    test_title = "Test Post #1"
    test_text = "test text"
    test_create_date = datetime.fromtimestamp(1326244364, tz=pytz.UTC)
    test_publish_date = datetime.fromtimestamp(1326244375, tz=pytz.UTC)

    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", email="", password="Passw0rd"
        )
        Post.objects.create(
            post_id=self.test_post_id,
            author=self.user,
            title=self.test_title,
            text=self.test_text,
            created_date=self.test_create_date,
            publish_date=self.test_publish_date,
        )

    def test_all_fields_set(self):
        test_post = Post.objects.get(post_id=self.test_post_id)
        self.assertEqual(test_post.author, self.user)
        self.assertEqual(test_post.title, self.test_title)
        self.assertEqual(test_post.text, self.test_text)
        self.assertEqual(test_post.created_date, self.test_create_date)
        self.assertEqual(test_post.publish_date, self.test_publish_date)

