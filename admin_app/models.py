from django.db import models
from custom_user.models import CustomUser

class Admins(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Admins'