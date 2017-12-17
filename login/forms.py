from django import forms
import django.contrib.auth.forms
from django.contrib.auth.models import User


class Loginform(forms.Form):
    Username = forms.CharField(max_length=30, required=True, help_text='Your Login ID.')
    Password = forms.CharField(max_length=50, required=True, help_text='Your Password.')


