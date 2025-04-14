from django.forms import ModelForm
from .models import AdminStaff

class AdminStaffRegistrationForm(ModelForm):
    class Meta:
        model = AdminStaff
        fields = ['name', 'email', 'password']