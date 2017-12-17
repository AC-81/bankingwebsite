from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render

def index(request):
    return HttpResponse("Hello World!!")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    for i in range(question.choice_set.count()):
        try:
            selected_choice = question.choice_set.all()[i]
            selected_choice.votes = request.POST['choice'+str(i+1)]
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice"
               })
        else:
            selected_choice.save()
    return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def latest_2_views(request):
    latest_2 = Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_2,
    }
    return HttpResponse(template.render(context, request))
