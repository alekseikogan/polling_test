from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Choice, Question, Survey


# Get questions and display them
def index(request):
    surveys = Survey.objects.all()
    context = {'surveys': surveys}
    return render(request, 'poller/index.html', context)


# Show specific question and choices
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Страницы с таким вопросом не существует :(")
#     return render(request, 'poller/detail.html', {'question': question})

def survey(request, survey_id):
    survey = Survey.objects.get(pk=survey_id)
    questions = Question.objects.filter(survey_id=survey_id)
    return render(
        request,
        'poller/survey.html',
        {
            'survey': survey,
            'questions': questions
        }
    )


# Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'poller/results.html', {'question': question})


# Vote for a question choice
def vote(request, question_id):
    print(f'request.POST = {request.POST}')
    question = Question.questions.get(id=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poller/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


# # Vote for a question choice
# def vote(request, question_id):
#     # print(request.POST['choice'])
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'poller/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args =(question.id, )))
