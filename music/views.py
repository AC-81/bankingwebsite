from django.views import generic
from .models import Album
from django.http import HttpResponse
from django.template import loader


class IndexView(generic.ListView):

    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()



class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

def service(request):

    t=loader.get_template('music/service.html')
    return HttpResponse(t.render({},request))

def disclaimer(request):
    t=loader.get_template('music/disclaimer.html')
    return HttpResponse(t.render({},request))

