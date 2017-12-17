from django.conf.urls import include , url
from . import views
from django.contrib.auth.views import login


app_name = 'login'
urlpatterns = [
    url(r'^$' , login  , {'template_name':'login/login.html'},name="login"),
    url(r'^profile/$' , views.home , name="home"),
]