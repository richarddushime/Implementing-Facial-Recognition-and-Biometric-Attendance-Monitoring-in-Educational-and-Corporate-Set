
from django.urls import path
from . import views
from .views import adminstaff_registration

urlpatterns = [
    path('register/', adminstaff_registration, name='adminstaff_registration'),
]
