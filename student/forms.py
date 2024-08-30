from django import forms
from .models import SubmittedAssignment

class SubmitAssignmentForm(forms.ModelForm):
    class Meta:
        model = SubmittedAssignment
        fields = ['submission']