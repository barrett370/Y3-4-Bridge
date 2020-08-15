from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
import uuid


class Post(models.Model):
    post_id = models.CharField(
        max_length=100, blank=True, unique=True, default=uuid.uuid4
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Course(models.Model):
    course_id = models.CharField(
        max_length=100, blank=True, unique=True, default=uuid.uuid4
    )
    tile: str
    description: str
    completion_date: datetime
    grade: str


class CV(models.Model):

    title = "Sam Barrett: CV"
    name = "Sam Barrett"
    address = models.TextField()
    phone_number = models.CharField(max_length=14)
    email_address = models.CharField(max_length=50)
    last_updated = models.DateTimeField(blank=True, null=True)
    tech_skills = ["Django", "Python"]
    education = {
        "University": [{}],
        "A_levels": [
            {"Computer Science": "A", "Physics": "C", "Futher Mathematics AS": "A",}
        ],
        "gcses": [{""}],
        "misc": [{}],
    }

    def publish(self):
        self.last_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.title
