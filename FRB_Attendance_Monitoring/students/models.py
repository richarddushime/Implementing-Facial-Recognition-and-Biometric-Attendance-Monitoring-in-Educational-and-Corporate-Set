from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid 


class Student(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    email = models.EmailField(db_index=True, max_length=200, unique=True)
    password = models.CharField(max_length=230, blank=True)
    is_superuser = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    id_number = models.CharField(max_length=20, blank=True)
    date_of_birth = models.CharField(max_length=20, blank=True)
    course_unit = models.CharField(max_length=10)
    major = models.CharField(max_length=150, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    
    groups = models.ManyToManyField(Group, related_name="students")
    user_permissions = models.ManyToManyField(Permission, related_name="students")
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        unique_together = ['id', 'email']
    
    
    def __str__(self) -> str:
        return f'{self.email}'

    
    



    