from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
#     last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     mobile = forms.CharField(max_length=10, required=True, help_text='Required.')
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'mobile')

class EditProfileForm(forms.ModelForm):
	class Meta(object):
		model = Profile
		fields = ['first_name','last_name','birthdate','emailid']