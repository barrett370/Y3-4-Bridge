# Generated by Django 3.1 on 2020-08-20 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_course_course_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='completion_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
