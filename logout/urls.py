from django.conf.urls import include , url
from . import views
from django.contrib.auth.views import logout


app_name = 'logout'
urlpatterns = [
    url(r'^$' , logout  , {'template_name':'logout/logoutsuccess.html'},name="logout"),
   ]