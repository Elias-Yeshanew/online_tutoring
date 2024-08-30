from django.shortcuts import render, redirect, get_object_or_404
from course.models import Assignment
from .forms import SubmitAssignmentForm
from .models import Students

def student_view(request):
    return render(request, 'student/index.html')


# def view_courses(request):
#     student = get_object_or_404

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