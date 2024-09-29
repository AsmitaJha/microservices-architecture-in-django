from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add related_name to resolve clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Prevents reverse accessor clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Prevents reverse accessor clash
        blank=True
    )
