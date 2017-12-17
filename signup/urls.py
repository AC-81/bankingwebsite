from django.contrib.auth import views as auth_views

from django.conf.urls import include , url
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

app_name = 'signup'

urlpatterns=[
    url(r'^$',CreateView.as_view(template_name='signup/signup.html',
             form_class=UserCreationForm,success_url='firsttime'), name="home"),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^firsttime/$',views.edit_profile,name='editprofile'),
    #url(r'^successsignup/$' , views.success , name="success")
]