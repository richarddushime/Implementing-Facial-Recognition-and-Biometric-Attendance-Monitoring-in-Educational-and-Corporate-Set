from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')