from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import  CustomUser

def home(request):
    return render(request, 'custom_user/index.html')

# def register(request):
#     if request.method=='POST':
#         form=CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)

#             role = form.cleaned_data.get('role', 'default_role')

#             user.role = role
#             user.save()
#             messages.success(request, "registration successful.")
#             # if role == 'family':
#             #     related_student_id = request.POST.get('related_student')
#             #     related_student = Students.objects.get(id=related_student_id)
#             #     Families.objects.create(user=user, related_student=related_student)
#             # login(request, user)
#             return redirect('login')
#     else:
#         form=CustomUserCreationForm()
    
#     return render(request, 'custom_user/register.html', {'form': form})

from django.contrib import messages  # Make sure to import this for success message

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # The role has already been handled in the form's save() method
            user.save()
            messages.success(request, "Registration successful.")  # Fix typo (seccessful -> successful)

            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'custom_user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                if user.is_teacher:
                    return redirect('teachers_home')
                if user.is_superuser:
                    return redirect('admin_dashboard')
                if user.is_student:
                    return redirect('students_home')
                if user.is_family:
                    return redirect('families_homepage')
    else:
        form = AuthenticationForm()
    
    return render(request, 'custom_user/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')

def update_user(request, pk):
    from teacher.models import Teachers
    from student.models import Students
    from admin_app.models import Admins
    from family.models import Families
    
    user = get_object_or_404(CustomUser, pk=pk)
    original_role = None

    if user.is_teacher:
        original_role = 'teacher'
    elif user.is_family:
        original_role = 'family'
    elif user.is_student:
        original_role = 'student'
    else:
        original_role = 'admin'

    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            new_username = form.cleaned_data['username']
            new_role = form.cleaned_data['role']

            # Check if the username has changed
            if new_username != user.username:
                if CustomUser.objects.filter(username=new_username).exclude(pk=user.pk).exists():
                    form.add_error('username', 'A user with that username already exists.')
                else:
                    user.username = new_username
            # Reset all roles to False
            user.is_teacher = False
            user.is_student = False
            user.is_family = False
            user.is_superuser = False

            # Check if the role has changed
            if original_role != new_role:
                if original_role == 'teacher':
                    Teachers.objects.filter(user=user).delete()
                elif original_role == 'family':
                    Families.objects.filter(user=user).delete()
                elif original_role == 'student':
                    Students.objects.filter(user=user).delete()
                else:
                    Admins.objects.filter(user=user).delete()

                if new_role == 'teacher':
                    user.is_teacher = True
                    Teachers.objects.update_or_create(user=user)
                elif new_role == 'student':
                    user.is_student = True
                    Students.objects.update_or_create(user=user)
                elif new_role == 'family':
                    user.is_family = True
                    Families.objects.update_or_create(user=user)
                else:
                    user.is_superuser = True
                    Admins.objects.update_or_create(user=user)

            user.save()
            return redirect('user_management')
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, 'custom_user/user_update.html', {'form': form})
