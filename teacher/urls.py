from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeachersHome, name='teachers_home'),
    path('assingment/', views.create_assignment, name='create_assignment'),
    path('assingment_list/', views.assignment_list, name='assignment_list'),
    path('courses/', views.teacher_courses, name='teacher_courses'),
    path('update_assignment/<int:pk>/', views.update_assignment, name='update_assignment'),
    path('delete_assignment/<int:pk>/', views.delete_assignment, name='delete_assignment'),

]