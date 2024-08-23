from django.shortcuts import render

def families_homepage(request):
    return render(request, 'family/index.html')