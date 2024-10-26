from django.shortcuts import render, redirect, get_object_or_404
from course.forms import AssignmentForm
from course.models import Assignment, CourseTeacher,Lesson
from .models import Teachers
from .forms import TeachersForm, LessonForm

def TeachersHome(request):
    return render(request, 'teacher/index.html')

def assignment_list(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments':assignments
        }
    return render(request, 'course/assignment_list.html', context)
    teacher/views.py
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

def delete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id = lesson_id)
    if request.method == 'POST':
        lesson.delete()
        return redirect('list_lessons')
    
    context = {
        'lesson':lesson
    }

    return render(request, 'teacher/delete_lesson.html', context)



def teacher_courses(request):
    teacher = get_object_or_404(Teachers, user = request.user)
    teacher_courses = CourseTeacher.objects.filter(teacher = teacher).select_related('course')

    context = {
        'courses':[cs.course for cs in teacher_courses],
    }

    return render(request, 'teacher/courses.html', context)

def create_lesson(request):
    teacher = get_object_or_404(Teachers, user = request.user)
    course_teacher_qs = CourseTeacher.objects.filter(teacher = teacher) 

    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.save()
            return redirect('lessons_view')
    else:
        form = LessonForm()

    form.fields['course'].queryset = course_teacher_qs

    context = {
        'form':form
    }

    return render(request, 'teacher/create_lesson.html', context)

def list_lessons(request):
    teacher = get_object_or_404(Teachers, user=request.user)

    course_teacher_qs = CourseTeacher.objects.filter(teacher = teacher)

    if course_teacher_qs.exists():
        lessons = Lesson.objects.filter(course__in = course_teacher_qs)
        print(lessons)
    else:
        lessons = Lesson.objects.none()

    context = {
        'lessons':lessons
    }

    return render(request, 'teacher/lesson_list.html', context)

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    
    context = {
        'lesson':lesson
    }

    return render(request, 'teacher/lesson_detail.html', context)

def update_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    if request.method == "POST":
        form = LessonForm(reques.POST, instance=lesson)
        if form.is_valid():
            lesson = form.save(commit = False)
            lesson.save()
            return redirect('list_lesson')
    else:
        form = LessonForm(instance = lesson)
    
    context = {
        "form":form,
        "lesson":lesson
    }
    
    return render(request, 'teacher/update_lesson.html', context)

def updateProfile(request):
    try:
        profile = request.user.teachers
    except Teachers.DoesNotExist:
        profile = None

    if request.method == "POST":
        form = TeachersForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # profile = form.save(commit=false)
            # profile.user = request.user
            # profile.save()
            form.save()
            return redirect('profile_view')
    else:
        form = TeachersForm(instance=profile)
        
    return render(request, "teacher/profile_form.html", {"form":form})

def profile_view(request):
    profile = Teachers.objects.get(user = request.user)
    # profile = get_object_or_404(TeachersForm, user_username = username)
    return render(request, "teacher/profile_view.html",{
        "profile":profile,
        "username":request.user.username
    })