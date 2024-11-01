from django.urls import path
from . import views

urlpatterns=[
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('user_management/', views.user_management, name='user_management'),
    path('user/<int:pk>/delete/', views.delete_user, name='delete_user'),  
]