from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreattionForm(UserCreationForm):
    ROLE_CHOICES =[
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('admin', 'admin'),
    ]

    role= forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model=CustomUser
        fields=('username','email', 'role', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data['role']

        # Reset all roles to False
        user.is_admin = False
        user.is_teacher = False
        user.is_student = False

        # Set the selected role to True
        if role == 'admin':
            user.is_admin = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'student':
            user.is_student = True

        if commit:
            user.save()
        return user