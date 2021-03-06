# Generated by Django 3.1 on 2020-08-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_course_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='course',
            name='grade',
            field=models.CharField(default='A', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='tile',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]
