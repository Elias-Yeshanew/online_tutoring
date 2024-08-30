from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_view, name='students_home'),
    path('assignment/<int:assignment_id>', views.submit_assignment, name='submit_assignment'),
]