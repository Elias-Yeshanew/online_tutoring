from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_view, name='students_home'),
    path('courses/', views.student_courses, name='student_courses'),
    path('assignment/<int:assignment_id>', views.submit_assignment, name='submit_assignment'),
    # path('student_courses/', views.student_courses, name='student_courses'),
    path('enroll_course/<int:course_id>', views.enroll_student_in_course, name='enroll_course'),
]