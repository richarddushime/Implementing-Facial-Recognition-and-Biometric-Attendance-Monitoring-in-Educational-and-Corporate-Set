from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')

def admincontact(request):
    return render(request, 'contact.html')