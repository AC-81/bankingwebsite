from django.conf.urls import include , url
from . import views
app_name = 'contact'


urlpatterns = [

    url(r'^$' ,views.index , name="index"),

    url(r'^write/$', views.write, name='write'),


]