from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
        ('normal', 'Normal User'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='normal')

