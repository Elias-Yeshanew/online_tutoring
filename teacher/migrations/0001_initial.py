# Generated by Django 5.0.7 on 2024-10-26 07:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstName', models.CharField(blank=True, max_length=255)),
                ('lastName', models.CharField(blank=True, max_length=255)),
                ('phoneNumber', models.CharField(blank=True, max_length=13)),
                ('qualification', models.TextField(blank=True)),
                ('availabilty', models.CharField(blank=True, max_length=255)),
                ('profilePicture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('experience', models.CharField(blank=True, max_length=255)),
                ('teachingPhilosophy', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Teachers',
            },
        ),
    ]
