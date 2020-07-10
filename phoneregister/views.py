from random import randint

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import MyUser
from django.contrib.auth import login
from . import forms
from . import helper


def phone_login(request):
    if 'phone_number' in request.POST:
        user = MyUser.objects.get(phone_number=request.POST.get('phone_number'))
        login(request, user)
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'phone_login.html')


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            otp = randint(10000, 99999)
            print('otp:', otp)
            new_user.is_active = False
            new_user.otp = otp
            new_user.save()
            request.session['user_info'] = new_user.phone_number
            print(new_user.phone_number)
            return HttpResponseRedirect(reverse('verify'))

    return render(request, 'signup.html')


def verify(request):

    if request.session.get('user_info'):
        print(request.session.get('user_info'))

    user = MyUser.objects.get(phone_number=request.session.get('user_info'))

    if request.method == "POST":
        if user.otp == int(request.POST.get('otp')):
            user.is_active = True
            user.save()
            return HttpResponseRedirect(reverse('dashboard'))

    return render(request, 'verify.html', {'phone_number': user.phone_number})


@login_required
def dashboard(request):

    if helper.check_otp_expiration(request.user.phone_number):
        return render(request, 'dashboard.html')
    return HttpResponseRedirect(reverse('phone_login'))
