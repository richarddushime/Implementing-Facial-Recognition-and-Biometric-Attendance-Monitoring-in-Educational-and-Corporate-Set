
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home" ),
    path('',views.student_dashboard, name="student_dashboard"),
]
