from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.template import loader
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.db import transaction
from django.core.mail import EmailMessage,send_mail
from .forms import EditProfileForm
from django.contrib.auth.models import User
from django import forms
from random import randint


def home(request):
    return render(request, 'signup/signup.html')


def edit_profile(request):
    uid = request.user
    fl=False
    try:
        fl=True
        profile = Profile.objects.get(userid=uid)
        data={
        'first_name':profile.first_name,
        'last_name':profile.last_name,
        'birthdate':profile.birthdate,
        'emailid':profile.emailid,
        'account_number':profile.account_number,
        'account_balance':profile.account_balance,
        }
    except:
        data={
        'first_name':'',
        'last_name':'',
        }
    form = EditProfileForm(request.POST or None,initial=data)
    if form.is_valid():
        p = form.save(commit=False)
        p.userid = request.user
        p.account_number= randint(10**8 , 10 **12)
        p.save()
        t = loader.get_template('signup/successsignup.html')
        return HttpResponse(t.render({}, request))
    context = {
        "form": form,
    }
    return render(request, 'signup/firstlogin.html', context)




# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             t = get_template('signup/successsignup.html')
#             return HttpResponse(t.render({}, request))
#     else:
#         form = SignUpForm()
#     return render(request, 'signup/signup.html', {'form': form})
