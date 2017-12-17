from django.conf.urls import url, include
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.latest_2_views, name='latest_2_views'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/result/$', views.result, name='result'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
