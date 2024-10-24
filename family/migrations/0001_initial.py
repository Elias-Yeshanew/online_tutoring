# Generated by Django 5.1.2 on 2024-10-12 22:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_user', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Families',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('related_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.students')),
            ],
            options={
                'verbose_name_plural': 'Families',
            },
        ),
    ]
