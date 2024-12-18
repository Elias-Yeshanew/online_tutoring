# Generated by Django 5.0.7 on 2024-10-26 07:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='SubmittedAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', models.FileField(upload_to='assignments/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.students')),
            ],
        ),
    ]
