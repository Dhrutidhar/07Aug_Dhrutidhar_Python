# Generated by Django 5.0.1 on 2024-02-03 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance_App', '0008_delete_userpolicies_alter_user_policies_grant_policy'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_policies_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fullname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=100)),
                ('mobile_number', models.BigIntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('select_type', models.CharField(max_length=500)),
                ('grant_policy', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='user_policies',
        ),
    ]