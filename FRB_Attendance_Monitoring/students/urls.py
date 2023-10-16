
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index" ),
    path('',views.student_dashboard, name="student_dashboard"),
]
