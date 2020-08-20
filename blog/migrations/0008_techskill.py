# Generated by Django 3.1 on 2020-08-20 16:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200820_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(default=None)),
                ('experience_amount', models.CharField(max_length=20)),
            ],
        ),
    ]