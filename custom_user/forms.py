from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

ROLE_CHOICES =[
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('family', 'family'),
    ]

class CustomUserCreattionForm(UserCreationForm):
    
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model=CustomUser
        fields=['username','email', 'role', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data['role']

        # Reset all roles to False
        # user.is_admin = False
        user.is_teacher = False
        user.is_student = False
        user.is_family = False

        # Set the selected role to True
        if role == 'family':
            user.is_family = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'student':
            user.is_student = True

        if commit:
            user.save()
        return user

class CustomUserUpdateForm(UserChangeForm):
    
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password']
    
