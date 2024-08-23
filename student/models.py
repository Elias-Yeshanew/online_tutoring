from django.db import models
from custom_user.models import CustomUser

class Students(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Students'