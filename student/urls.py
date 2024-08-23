from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_view, name='students_home')
]