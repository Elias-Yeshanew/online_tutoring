from django.shortcuts import render, redirect, get_object_or_404
from course.models import Assignment
from .forms import SubmitAssignmentForm
from .models import Students
from course.models import Enrollment, CourseStudent, Courses,CourseTeacher

def student_view(request):
    return render(request, 'student/index.html')

def student_courses(request):
    student = get_object_or_404(Students, user = request.user)
    course_students = CourseStudent.objects.filter(student=student).select_related('course_course','course_teacher')
    
    courses = [{'course': cs.course.course, 'teacher':cs.course.teacher} for cs in course_students]

    context = {
        'courses':courses
    }

    return render(request, 'teacher/courses.html', context)

def enroll_student_in_course(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    
    # Ensure there’s an associated teacher for this course
    course_teacher_qs = CourseTeacher.objects.filter(course=course)
    
    if not course_teacher_qs.exists():
        # messages.error(request, "No teacher is offering this course.")
        return redirect('student_courses')
    
    student = get_object_or_404(Students, user=request.user)
    
    # Check if student is already enrolled in any session of this course
    if CourseStudent.objects.filter(student=student, course__course=course).exists():
        # messages.info(request, "You are already enrolled in this course.")
        return redirect('student_courses')
    
    # Enroll the student with the first available teacher for this course
    course_teacher = course_teacher_qs.first()
    CourseStudent.objects.create(student=student, course=course_teacher)
    
    # messages.success(request, f"Enrolled in {course.title} with {course_teacher.teacher.user.username}.")
    return redirect('student_courses')
  
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