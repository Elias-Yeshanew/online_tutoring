from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeachersHome, name='teachers_home')
]