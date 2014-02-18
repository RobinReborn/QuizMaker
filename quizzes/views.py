from django.shortcuts import render
from django.http import HttpResponse
from quizzes.models import *
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response

#from helper_functions import process_Quiz
from django.http import QueryDict
from django.core.context_processors import csrf
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

@csrf_protect
def quiz_create(request):
    c = {}
    c.update(csrf(request))
    template = loader.get_template('quizzes/quiz_create.html')
    #return render(request,'quizzes/quiz_create.html')
    return render_to_response("quizzes/quiz_create.html", c)

@csrf_protect
def created(request):
    #process_Quiz(request)
    results = request.POST
    print results
    template = loader.get_template('quizzes/quiz_created.html')
    context = {"results": results}
    #here we do some stuff to add the quiz, questions and results to our DB
    quiz = Quiz()
    quiz.Quiz_Title = request.POST['Quiz_Name']
    quiz.Quiz_Description = request.POST['Quiz_Description']
    #here's the tricky part, we need to add the questions and results
    
    #first we count the number of questions
	#this can be used to loop through all the questions then save them
	question_1 = results.get('question_1',None)
    total_questions = 0
    #for key in quiz:
    #    if (re.match(r'question\d',key)):
    #        total_questions = total_questions+1
    #there are question * results number of r1's
    #total_results = len(test.getlist('r3')[0])/total_questions
    #then we need to associate them with the quiz we're dealing with
    #then we need to have them both associated with the right quiz
    return render(request,'quizzes/quiz_created.html',context) 
   # Create your views here.
