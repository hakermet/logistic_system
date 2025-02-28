from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=[
            ('admin', 'Admin'),
            ('dispatcher', 'Dispatcher'),
            ('driver', 'Driver'),
        ],
        default='dispatcher'
    )

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Унікальна назва для зв'язку
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Унікальна назва для зв'язку
        blank=True
    )
    telegram_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username
