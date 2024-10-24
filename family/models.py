from django.db import models
from custom_user.models import CustomUser
from student.models import Students

class Families(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    related_student = models.ForeignKey(Students, on_delete=models.CASCADE,null=True, blank=True )

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name_plural = 'Families'

