from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .usermanager import UserManager

# Create your models here.


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = None
    phone_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField( max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff =  models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = []