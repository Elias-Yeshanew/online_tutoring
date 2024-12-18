from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        email=self.normalize_email(email)
        extra_fields.setdefault('is_active',True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    is_admin=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    is_family=models.BooleanField(default=False)

    profilePicture = models.ImageField(upload_to = 'profile_pictures/', null= True, blank=True)
    phoneNumber = models.CharField(max_length = 13, blank=True)

    objects= CustomUserManager()
