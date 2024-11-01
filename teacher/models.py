from django.db import models
from custom_user.models import CustomUser

class Teachers(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    qualification = models.TextField(blank=True)
    availability  = models.CharField(max_length=255, blank=True)
    experience = models.CharField(max_length=255, blank=True)
    teachingPhilosophy = models.TextField(blank=True)
 
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Teachers'

