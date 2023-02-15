from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string




class UserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(
                'Email field is required'
            )
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.create_activation_code()
        user.save()
        user.is_active = False
        user.is_superuser = False
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError(
                'Email is required'
            )
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    

class User(AbstractUser):

    CHOICES = (
        ('US', 'United States'),
        ('RU', 'Russia'),
        ('KG', 'Kyrgyzstan'),
        ('KZ', 'Kazakhastan'),
    )

    username = models.CharField(max_length=60, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, blank=True)
    country = models.CharField(max_length=300, choices=CHOICES)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=55, blank=True)
    password = models.CharField(max_length=100)
    password_confirm = models.CharField(max_length=100)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'{self.email} -> {self.id}'

    def create_activation_code(self):
        code = get_random_string(length=10, allowed_chars='1234567890#!@$%^&*_')
        self.activation_code = code
    password = models.PositiveIntegerField()
    
