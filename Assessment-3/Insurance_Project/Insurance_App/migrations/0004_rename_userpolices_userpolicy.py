# Generated by Django 5.0.1 on 2024-01-30 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance_App', '0003_userpolices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userpolices',
            new_name='userpolicy',
        ),
    ]
