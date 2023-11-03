from django.shortcuts import render, redirect
from .forms import AdminStaffRegistrationForm

def adminstaff_registration(request):
    if request.method == 'POST':
        form = AdminStaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_dashboard')
    else:
        form = AdminStaffRegistrationForm()
    context = {'form': form}
    return render(request, 'adminstaff_registration.html', context)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')

def admincontact(request):
    return render(request, 'contact.html')