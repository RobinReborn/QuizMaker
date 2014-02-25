from django.shortcuts import render
from django.http import HttpResponse
from quizzes.models import *
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
import re
import string
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
    for q in quiz_request.questions.all():
        if (q != ','):
            quiz_questions.append(q)
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
    data = request.POST.dict()

    #print results
    template = loader.get_template('quizzes/quiz_created.html')
    #here we do some stuff to add the quiz, questions and results to our DB
    quiz = Quiz()
    quiz.Quiz_Title = request.POST['Quiz_Name']
    quiz.Quiz_Description = request.POST['Quiz_Description']
	#quiz.save()
    quiz.save()
	
    #here's the tricky part, we need to add the questions and results
    #first we count the number of questions
	#this can be used to loop through all the questions then save them
	#question_1 = results.get('question_1',None)
    total_questions = 0
    total_results = 0
    for key in data:
		#this deals with the questions
        if (re.match(r'question\d',key)):
            total_questions = total_questions+1
            question = Question()
            question.question_text = data.__getitem__(key)
            question.answer1 = data['answer1_q' + str(total_questions)]
            question.answer2 = data['answer2_q' + str(total_questions)]
            question.answer3 = data['answer3_q' + str(total_questions)]
            question.answer4 = data['answer4_q' + str(total_questions)]
            question.save()
            quiz.questions.add(question)
            quiz.save()
	for key in data:
		#this deals with results
		if (re.match(r'result\d*$',key)):
			print key
			total_results = total_results +1
			result = Result()
			result.save()
			result.Quiz_Result = data[key]
			result_num = key[6:]
			result_number = "result_explanation" + result_num
			result_number = string.strip(result_number,"'")
			result_number = string.strip(result_number,'"')
			result.Quiz_Result_Explanation = data[result_number]
			#this is the hard part, getting the scoring for each result
			#each question has four numbers, we use the appropriate index to get them
			scoring_list = [None] * (4 * (total_questions + 1))
			for x in range(1, 4):
				scoring_list[0] = data['r1_' + result_num]
				scoring_list[1] = data['r2_' + result_num]
				scoring_list[2] = data['r3_' + result_num]
				scoring_list[3] = data['r4_' + result_num]
			result.Quiz_Scoring = scoring_list
			result.save()
			quiz.results.add(result)
			quiz.save()
	
	quiz_questions = []
	quiz_results = []
	for q in quiz.questions.all():
		if (q != ','):
			quiz_questions.append(q)
	for r in quiz.results.all():
		if (r != ','):
			quiz_results.append(r)
	context = {"results": data, "quiz_questions": quiz_questions, "quiz_results": quiz_results}
    return render(request,'quizzes/quiz_created.html',context) 
