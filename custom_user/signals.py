from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from teacher.models import Teachers
from student.models import Students
from family.models import Families
from admin_app.models import Admins


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            Teachers.objects.create(user=instance)
        elif instance.is_student:
            Students.objects.create(user=instance)
        elif instance.is_admin:
            Admins.objects.create(user=instance)
        elif instance.is_family:
            Families.objects.create(user=instance)

