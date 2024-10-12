from django.shortcuts import render, redirect, get_object_or_404
from course.forms import AssignmentForm
from course.models import Assignment, CourseTeacher
from .models import Teachers

def TeachersHome(request):
    return render(request, 'teacher/index.html')

def assignment_list(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments':assignments
        }
    return render(request, 'course/assignment_list.html', context)
    
def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():

            form.save()

            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    
    context = {
        'form':form
    }
    return render(request, 'course/create_assignment.html', context)


def update_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm(instance=assignment)
    
    context = {
        'form':form
    }
    return render(request, 'course/update_assignment.html', context)


def delete_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        assignment.delete()
        return redirect('assignment_list')

    context = {
        'assignment':assignment
    }
    return render(request, 'course/delete_assignment.html', context)


def teacher_courses(request):
    teacher = get_object_or_404(Teachers, user = request.user)
    teacher_courses = CourseTeacher.objects.filter(teacher = teacher).select_related('course')

    context = {
        'courses':[cs.course for cs in teacher_courses],
    }

    return render(request, 'teacher/courses.html', context)