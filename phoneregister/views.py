from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import MyUser
from django.contrib.auth import login, logout
from . import forms
from . import helper
from django.contrib import messages


def signup(request):
    form = forms.SignUpForm()

    if request.method == "POST":
        try:
            if "phone_number" in request.POST:
                phone_number = request.POST.get('phone_number')
                user = MyUser.objects.get(phone_number=phone_number)
                otp = helper.get_random()
                helper.send_otp(user.phone_number, otp)
                user.otp = otp
                user.save()
                request.session['user_info'] = user.phone_number
                return HttpResponseRedirect(reverse('verify'))

        except MyUser.DoesNotExist:
            form = forms.SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                otp = helper.get_random()
                helper.send_otp(user.phone_number, otp)
                user.is_active = False
                user.otp = otp
                user.save()
                request.session['user_info'] = user.phone_number
                return HttpResponseRedirect(reverse('verify'))

    return render(request, 'signup.html', {'form': form})


def verify(request):

    try:
        user = MyUser.objects.get(phone_number=request.session.get('user_info'))

        if request.method == "POST":

            if not helper.check_otp_expiration(user.phone_number):
                messages.error(request, 'OTP is expired, please try again.')
                return HttpResponseRedirect(reverse('signup'))

            if user.otp != int(request.POST.get('otp')):
                messages.error(request, 'OTP is incorrect.')
                return HttpResponseRedirect(reverse('verify'))

            user.is_active = True
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))

        return render(request, 'verify.html', {'phone_number': user.phone_number})

    except MyUser.DoesNotExist:
        messages.error(request, 'Error accorded, try again.')
        return HttpResponseRedirect(reverse('signup'))


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('signup'))

