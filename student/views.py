from django.shortcuts import render

def student_view(request):
    return render(request, 'student/index.html')
