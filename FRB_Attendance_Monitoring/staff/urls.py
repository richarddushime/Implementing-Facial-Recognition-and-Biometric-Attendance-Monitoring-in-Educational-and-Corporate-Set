
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index" ),
    path('staff_dashboard/',views.staff_dashboard, name="staff_dashboard"),
    path('admincontact/', views.admincontact, name="admincontact"),
]
