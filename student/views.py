from django.shortcuts import render, redirect, get_object_or_404
from course.models import Assignment
from .forms import SubmitAssignmentForm
from .models import Students
from course.models import Enrollment, CourseStudent, Courses

def student_view(request):
    return render(request, 'student/index.html')

def student_courses(request):
    student = get_object_or_404(Students, user=request.user)
    course_students = CourseStudent.objects.filter(student=student).select_related('course')

    context = {
        'courses': [cs.course for cs in course_students],
    }

    return render(request, 'student/courses.html', context)


def enroll_student_in_course(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    student = get_object_or_404(Students, user=request.user)
    
    # Check if the student is already enrolled
    if not CourseStudent.objects.filter(student=student, course=course).exists():
        CourseStudent.objects.create(student=student, course=course)
    
    return redirect('student_courses')  # Or any other appropriate redirect


def submit_assignment(request, assignment_id):
    assignment  = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        form = SubmitAssignmentForm(request.POST, request.FILES)
        if form.is_valid:
            submission = form.save(commit=False)
            submission.student = get_object_or_404(Students, user=request.user)
            submission.assignment = assignment
            submission.save()
            return redirect('students_home')
    
    else:
        form = SubmitAssignmentForm()
    
    context = {
        'form':form
    }
    
    return render(request, 'student/submit_assignment.html', context)