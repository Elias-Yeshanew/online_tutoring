from django.db import models
from custom_user.models import CustomUser
# from family.models import Families



class Students(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # student_family = models.ForeignKey(Families, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Students'
    

class SubmittedAssignment(models.Model):
    
    from course.models import Assignment

    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submission = models.FileField(upload_to='assignments/')
    submitted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"student{student} submitted assignment {assignment} at {submitted_at}"