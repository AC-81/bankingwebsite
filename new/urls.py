
from django.conf.urls import include , url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include("music.urls",namespace="music"),name="music"),
    url(r'^contact/', include("contact.urls",namespace="contact"),name="contact"),
    url(r'^polls/', include('polls.urls',namespace="polls"), name='polls'),
    url(r'^signup/',include("signup.urls",namespace="signup"), name='signup'),
    url(r'^account/$',include("account.urls",namespace="account"),name="account"),
    url(r'^login/',include('login.urls',namespace="login"),name='login'),
    url(r'^logout/',include('logout.urls',namespace="logout"),name='logout'),
]



#	url(r'^accounts/register/$',
# CreateView.as_view(template_name='Election_Portal/register.html',
# form_class=UserCreationForm,success_url='/editprofile'),name='register'),
