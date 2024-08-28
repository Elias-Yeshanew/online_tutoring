from django.db import models
from custom_user.models import CustomUser


class Teachers(models.Model):
    user= models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # subjects=models.ManyToManyField('Subject')

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Teachers'

