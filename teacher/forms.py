from django import forms
from .models import Teachers
from course.models import Lesson

class TeachersForm(forms.ModelForm):
    
    class Meta:
        model = Teachers
        fields = "__all__"

class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        # fields = "__all__"
        fields = ['course', 'title', 'content', 'vidio_url', 'order']

    
    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
