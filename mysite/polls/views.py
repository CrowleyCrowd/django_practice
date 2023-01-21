from django.shortcuts import render
from django.http import HttpResponse #Renderiza texto
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date', 'question_text')[:5]
    #select from questions order by pub_date desc limit 5;
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail (request, question_id):
    question_to_display = Question.objects.get(pk=question_id)
