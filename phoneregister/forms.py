from django import forms
from . import models


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.MyUser
        fields = ['phone_number', ]
