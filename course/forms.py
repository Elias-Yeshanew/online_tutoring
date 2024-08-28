from django import forms
from .models import Courses, Assignment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'

class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = '__all__'
