from django import forms
import django.contrib.auth.forms
from django.contrib.auth.models import User


class WriteToUs(forms.Form):
    Subject = forms.CharField(max_length=30, required=True, help_text='What is it related to?' )
    Message = forms.CharField(max_length=1000, required=True, help_text='What do you want to say?',widget=forms.Textarea)


