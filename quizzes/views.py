from django.shortcuts import render
from django.http import HttpResponse
from quizzes.models import Quiz
from django.template import RequestContext, loader

def index(request):
    quiz_list = Quiz.objects.all()
    template = loader.get_template('quizzes/index.html')
    context = {'quiz_list': quiz_list}
    return render(request, 'quizzes/index.html', context)
def quiz(request,Quiz_Title):
    #quiz_request = Quiz.objects.get(Quiz_Title=quiz)
    template = loader.get_template('quizzes/quiz.html')
    context = {'Quiz_Title': Quiz_Title}
    return render(request, 'quizzes/quiz.html', context)  
   # Create your views here.
