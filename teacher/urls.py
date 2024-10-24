from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeachersHome, name='teachers_home'),
    path('assingment/', views.create_assignment, name='create_assignment'),
    path('assingment_list/', views.assignment_list, name='assignment_list'),
    path('courses/', views.teacher_courses, name='teacher_courses'),
    path('update_assignment/<int:pk>/', views.update_assignment, name='update_assignment'),
    path('delete_assignment/<int:pk>/', views.delete_assignment, name='delete_assignment'),
    path('profile_view/', views.profile_view, name='profile_view'),
    path('updateProfile/', views.updateProfile, name='updateProfile'),
    path('createLesson/', views.create_lesson, name='create_lesson'),
    path('lesson/', views.list_lessons, name='list_lessons'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('lesson/<int:lesson_id>/update', views.update_lesson, name='update_lesson'),
    path('lesson/<int:lesson_id>/delete', views.delete_lesson, name='delete_lesson'),

]