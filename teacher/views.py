from django.shortcuts import render

def TeachersHome(request):
    return render(request, 'teacher/index.html')
