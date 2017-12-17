from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail
from django.conf import settings
from . import forms
from django.template import loader


def index(request):
    t=loader.get_template('contact/index.html')
    return HttpResponse(t.render({},request))


def write(request):
    to_list = ['avi.chawlaavi@gmail.com']
    from_email = settings.EMAIL_HOST_USER


    if request.method == 'POST':
        form = forms.WriteToUs(request.POST)
        if form.is_valid():

            subject = form.cleaned_data.get('Subject')
            message = form.cleaned_data.get('Message')
            send_mail(subject, message, recipient_list=to_list, from_email=from_email,fail_silently=True)
            t = loader.get_template('contact/thanks.html')
            return HttpResponse(t.render({},request))
    else:
        form = forms.WriteToUs()
    return render(request, 'contact/write.html', {'form': form})



