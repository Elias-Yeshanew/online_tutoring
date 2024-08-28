from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/<int:pk>/update/', views.update_user, name='update_user'),

]