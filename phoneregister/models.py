from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin

from .usermanager import UserManager
import datetime

# Create your models here.


class MyUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=20, unique=True)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = []

    backend = 'phoneregister.backends.PhoneBackend'
