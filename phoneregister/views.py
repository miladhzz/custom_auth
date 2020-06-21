from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import MyUser
from .backends import PhoneBackend
from django.contrib.auth import authenticate, login

def phone_login(request):
    if 'phone_number' in request.POST:
        user = MyUser.objects.get(phone_number=request.POST.get('phone_number'))
        login(request, user, backend='phoneregister.backends.PhoneBackend')
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'phone_login.html')


def home(request):
    return render(request, 'home.html')