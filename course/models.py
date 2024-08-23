
from django.db import models
from teacher.models import Teachers
from student.models import Students

class CourseCategories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Courses(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(CourseCategories, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.title} with {self.teacher.user.username}"
