# Generated by Django 3.1 on 2020-08-20 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200820_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='tile',
            new_name='title',
        ),
    ]