from typing import Any
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)
from django.db import models
from ishiro.abstract.models import IshiroObject
from django.utils import timezone

class UserManager(BaseUserManager):

    def create(self, email, password=None, **extra_fields) :
        
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password(password)

        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        extra_fields['email'] = email

        return self.create_user(password, **extra_fields)

        
    

class User(IshiroObject, AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    joined = models.DateField(default=timezone.now())

    objects = UserManager()

    EMAIL_FIELDS = ['email']
    USERNAME_FIELD = 'email'

