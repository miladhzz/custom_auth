from . import models
import datetime


def check_otp_expiration(phone_number):
    user = models.MyUser.objects.get(phone_number=phone_number)
    print('user', user.phone_number)
    now = datetime.datetime.now()
    print('now', now)
    otp_time = user.otp_create_time
    difference_time = now - otp_time
    print('opt time', otp_time)
    print('difference (second):', difference_time.seconds)
    if difference_time.seconds > 120:
        return False
    return True


