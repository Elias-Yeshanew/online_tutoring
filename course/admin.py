from django.contrib import admin
from .models import Courses, CourseCategories, Enrollment

admin.site.register(Courses)
admin.site.register(CourseCategories)
admin.site.register(Enrollment)
