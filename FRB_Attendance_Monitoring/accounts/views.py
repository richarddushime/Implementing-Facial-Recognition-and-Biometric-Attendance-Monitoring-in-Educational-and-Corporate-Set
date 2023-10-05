from django.shortcuts import render, redirect, reverse
from .email_backend import EmailBackend
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib.auth import login, logout
# Create your views here.


def account_login(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect(reverse("staffDashboard"))
        else:
            return redirect(reverse("studentDashboard"))

    context = {}
    if request.method == 'POST':
        user = EmailBackend.authenticate(request, username=request.POST.get(
            'email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            if user.user_type == '1':
                return redirect(reverse("staffDashboard"))
            else:
                return redirect(reverse("studentDashboard"))
        else:
            messages.error(request, "Invalid details")
            return redirect("/")

    return render(request, "login.html", context)


def account_register(request):
    userForm = CustomUserForm(request.POST or None)
    studentForm = studentForm(request.POST or None)
    context = {
        'form1': userForm,
        'form2': studentForm
    }
    if request.method == 'POST':
        if userForm.is_valid() and studentForm.is_valid():
            user = userForm.save(commit=False)
            student = studentForm.save(commit=False)
            student.admin = user
            user.save()
            student.save()
            messages.success(request, "Account created. You can login now!")
            return redirect(reverse('account_login'))
        else:
            messages.error(request, "Provided data failed validation")
            # return account_login(request)
    return render(request, "stdent/reg.html", context)


def account_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        messages.success(request, "Thank you for visiting us!")
    else:
        messages.error(
            request, "You need to be logged in to perform this action")

    return redirect(reverse("account_login"))
