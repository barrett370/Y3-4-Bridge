from django.contrib import admin
from .models import Post, CV, Course, TechSkill


admin.site.register(Post)
admin.site.register(CV)
admin.site.register(Course)
admin.site.register(TechSkill)
