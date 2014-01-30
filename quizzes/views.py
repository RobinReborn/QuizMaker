from django.shortcuts import render
from django.http import HttpResponse
from quizzes.models import *
from django.template import RequestContext, loader

def index(request):
    quiz_list = Quiz.objects.all()
    template = loader.get_template('quizzes/index.html')
    context = {'quiz_list': quiz_list}
    return render(request, 'quizzes/index.html', context)
def quiz(request,Quiz_Name):
    quiz_request = Quiz.objects.get(Quiz_Title=Quiz_Name)
    quiz_questions = []
    for question in quiz_request.Quiz_Questions:
        if (question != ','):
            quiz_questions.append(Question.objects.get(id = question))
    template = loader.get_template('quizzes/quiz.html')
    context = {'quiz_request': quiz_request, 'quiz_questions': quiz_questions}
    return render(request, 'quizzes/quiz.html', context)  

def quiz_create(request):
    template = loader.get_template('quizzes/quiz_create.html')
    return render(request,'quizzes/quiz_create.html')

   # Create your views here.
