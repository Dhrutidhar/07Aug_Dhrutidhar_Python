# Generated by Django 5.0 on 2024-01-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Title', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=20)),
                ('Content', models.CharField(max_length=300)),
            ],
        ),
    ]
