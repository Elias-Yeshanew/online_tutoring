from django.contrib import admin
from .models import *

admin.site.register(Courses)
admin.site.register(CourseCategories)
admin.site.register(Enrollment)
admin.site.register(Assignment)
admin.site.register(CourseStudent)
admin.site.register(CourseTeacher)

