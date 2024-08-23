from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreattionForm

def home(request):
    return render(request, 'custom_user/index.html')

def register(request):
    if request.method=='POST':
        form=CustomUserCreattionForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('login')
    else:
        form=CustomUserCreattionForm()
    
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
                    return redirect('/admin/')
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