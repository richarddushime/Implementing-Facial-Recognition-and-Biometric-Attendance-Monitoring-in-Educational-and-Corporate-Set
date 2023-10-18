# students/forms.py

from django import forms
from django.core.validators import EmailValidator
from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('id', 'is_active', 'is_superuser', 'groups', 'user_permissions', 'is_staff',)
        
    # full_name = forms.CharField(
    #     max_length=255,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Full Name',
    #     })
    # )

    # id_number = forms.CharField(
    #     max_length=50,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'ID Number',
    #     })
    # )

    # email = forms.EmailField(
    #     validators=[EmailValidator()],
    #     widget=forms.EmailInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Email Address',
    #     })
    # )

    # date_of_birth = forms.DateField(
    #     widget=forms.DateInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'YYYY-MM-DD',
    #         'type': 'date',
    #     })
    # )

    # course_unit = forms.CharField(
    #     max_length=255,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Course Unit',
    #     })
    # )

    # major = forms.CharField(
    #     max_length=255,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Major',
    #     })
    # )
