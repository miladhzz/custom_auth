from . import models
import datetime
from random import randint


def check_otp_expiration(phone_number):
    user = models.MyUser.objects.get(phone_number=phone_number)
    now = datetime.datetime.now()
    otp_time = user.otp_create_time
    difference_time = now - otp_time
    print('difference (second):', difference_time.seconds)
    if difference_time.seconds > 120:
        return False
    return True


def get_random():
    return randint(1000, 9999)


def send_otp(phone_number, otp):
    print('otp:', otp)





