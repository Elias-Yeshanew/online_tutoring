from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Courses
from .forms import CourseForm

def course_list(request):
    courses = Courses.objects.all()
    return render(request, 'course/course_list.html', {'courses':courses})

@user_passes_test(lambda u: u.is_superuser or u.is_teacher)
def course_create(request):
    if request.method =='POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course/course_form.html', {'form':form})


@user_passes_test(lambda u: u.is_superuser or u.is_teacher)
def course_update(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course/course_form.html', {'form':form})

@user_passes_test(lambda u: u.is_superuser or u.is_teacher)
def course_delete(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course/course_confirm_delete.html', {'course':course})

