from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse

# Create your views here.
# def index(req):
#     return HttpResponse("<h1>Welcome to Poll App</h1>")

# def index(req):
#     ques = Question.objects.order_by('-pub_date')
#     output = ' '.join([q.question_text for q in ques])
#     return HttpResponse(output)

# def index(req):
#     ques = Question.objects.order_by('-pub_date')
#     temp = loader.get_template('index.html')
#     context = {
#         'questions' : ques
#     }
#     return HttpResponse(temp.render(context, req))

def index(req):
    ques = Question.objects.order_by('-pub_date')
    return render(req, 'index.html', {'questions' : ques})

# def detail(req, question_id):
#     ques = "<h2>You are on the detail page of ques %s</h2>"
#     return HttpResponse(ques % (question_id))

# def detail(req, question_id):
#     try:
#         ques = Question.objects.get(pk = question_id)
#     except Question.DoesNotExist:
#         return Http404("Question does not exist")
#
#     return render(req, 'details.html', {'question' : ques})

def detail(req, question_id):
    ques = get_object_or_404(Question, pk=question_id)
    return render(req, 'details.html', {'question': ques})

def result(req,question_id):
    ques = get_object_or_404(Question, pk=question_id)
    return render(req, 'result.html', {'question': ques})


# def vote(req,question_id):
#     return HttpResponse("<h2>You are on vote page</h2>")

def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk = req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(req, 'details.html',{
            'question' : question,
            'errorMessage' : "You didn't selected a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))