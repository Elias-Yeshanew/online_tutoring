from django.shortcuts import render, redirect, get_object_or_404
from course.models import Assignment
from .forms import SubmitAssignmentForm
from .models import Students
from course.models import Enrollment

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


# def student_courses(request):
#     # Assuming the student is logged in
#     student = get_object_or_404(Students, user=request.user)  # This assumes the request.user is a Student
#     enrollments = Enrollment.objects.filter(student=student)
#     courses = [enrollment.course for enrollment in enrollments]


#     context = {
#         'courses': courses,
#     }

#     print(context)
#     return render(request, 'student/courses.html', context)

def student_courses(request):
    student = get_object_or_404(Students, user=request.user)
    enrollments = Enrollment.objects.filter(student=student).select_related('student', 'course', 'teacher', 'student_family')
    
    courses_with_details = [(enrollment.course, enrollment.teacher, enrollment.student_family) for enrollment in enrollments]

    context = {
        'courses_with_details': courses_with_details,
    }
    print(context)

    return render(request, 'student/student_courses.html', context)

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