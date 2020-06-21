from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def example(reuqest):
    return HttpResponse('Response')


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    # It could make in this way or only in one return with render method
    # template = loader.get_template('polls/index.html')  # django.template.loader
    # return HttpResponse(template.render(context, request))

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # question = Question.objects.get(pk=question_id)  # It is valid get(id=question_id) as well
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        print(request.POST)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #  KeyError raise if choice wasn’t provided in POST data
        # Redisplay the question voting form with the error message
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Please select a choice...",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # reverse() function helps avoid having to hardcode a URL in the view
        # function. It is given the name of the view that we want to pass control to and
        # the variable portion of the URL pattern that points to that view.



