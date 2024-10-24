from django.contrib import admin
from .models import Teachers
from course.models import Lesson

admin.site.register(Teachers)
admin.site.register(Lesson)
