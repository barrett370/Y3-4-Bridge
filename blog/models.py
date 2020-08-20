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
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    completion_date = models.DateField()
    grade = models.CharField(max_length=200)
    course_level_choices = (("university", "University"), ("other", "Other"))
    course_level = models.CharField(
        choices=course_level_choices, max_length=20, default="university"
    )

    def __str__(self):
        return self.title


class TechSkill(models.Model):
    skill_id = models.CharField(
        max_length=100, blank=True, unique=True, default=uuid.uuid4
    )
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    experience_amount = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class CV(models.Model):

    title = "Sam Barrett: CV"
    name = "Sam Barrett"
    address = models.TextField()
    phone_number = models.CharField(max_length=14)
    email_address = models.CharField(max_length=50)
    last_updated = models.DateTimeField(blank=True, null=True)
    tech_skills = TechSkill.objects.all()
    university_modules = Course.objects.filter(course_level="university").order_by(
        "completion_date"
    )

    education = {
        "A levels": {
            "Mathematics": "A",
            "Computer Science": "A",
            "Physics": "C",
            "Futher Mathematics AS": "A",
        },
        "GCSEs": {
            "Mathematics": "A*",
            "English Language": "A*",
            "Chemistry": "A*",
            "English Literature": "A",
            "Physics": "A",
            "Biology": "A",
            "Religious Studies": "A",
            "History": "A",
            "Computer Science": "A",
            "French": "B",
            "Art": "C",
        },
    }
    misc_modules = Course.objects.filter(course_level="other").order_by(
        "completion_date"
    )
    # misc_modules = models.ManyToManyField(Course)

    def publish(self):
        self.last_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.title
