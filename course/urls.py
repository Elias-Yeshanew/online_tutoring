from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('new/', views.course_create, name='course_create'),
    path('<int:pk>/edit/', views.course_update, name='course_update'),
    path('<int:pk>/delete/', views.course_delete, name='course_delete'),
]