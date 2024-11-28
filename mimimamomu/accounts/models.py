from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Дополнительные поля, если нужно
    # Пример: роль пользователя
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.username
