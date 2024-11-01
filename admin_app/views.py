from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from custom_user.models import CustomUser
from custom_user.forms import CustomUserCreationForm

User = get_user_model()

@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    return render(request, 'admin_app/dashboard.html')

def user_management(request):
    users=get_user_model().objects.all()
    return render(request, 'admin_app/user_management.html', {'users': users})

def delete_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method =='POST':
        user.delete()
        return redirect('user_management')
    return render(request, 'admin_app/confirm_user_delete.html',{'user':user})


