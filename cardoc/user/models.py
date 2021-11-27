from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.password_validation import validate_password

from rest_framework.validators import ValidationError


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        try:
            if validate_password(password, user=user):
                return password
        except:
            raise ValidationError("incorrect validation")
        
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(max_length=256, unique=True)
    name = models.CharField(max_length=32, unique=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
