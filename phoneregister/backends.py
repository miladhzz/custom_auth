from django.contrib.auth.backends import ModelBackend

from .models import MyUser


class PhoneBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        phone_number = kwargs['phone_number']
        try:
            user = MyUser.objects.get(phone_number=phone_number)
            return user
        except MyUser.DoesNotExist:
            pass
