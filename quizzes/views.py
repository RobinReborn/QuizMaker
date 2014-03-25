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
@csrf_protect
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
	c = {'request' : request}
	c.update(csrf(request))
	template = loader.get_template('quizzes/quiz_create.html')
    #return render(request,'quizzes/quiz_create.html')
	return render_to_response("quizzes/quiz_create.html", c)

@csrf_protect
def result(request,Quiz_Name):
	quiz = Quiz.objects.get(Quiz_Title=Quiz_Name)
	results = []
	for r in quiz.results.all():
		if (r != ','):
			results.append(r)
	c = {'request' : request, 'results' : results}
	c.update(csrf(request))
	template = loader.get_template('quizzes/result.html')
	print results
	return render_to_response('quizzes/result.html',c)
@csrf_protect
def created(request):
    
	data = request.POST.dict()
	template = loader.get_template('quizzes/quiz_created.html')
    #here we do some stuff to add the quiz, questions and results to our DB
	quiz = Quiz()

	quiz.Quiz_Title = request.POST['Quiz_Name']
	quiz.Quiz_Description = request.POST['Quiz_Description']

	quiz.save()

	Results_List = data['All_Results']
	Results_Explanation_List = data['All_Results_Explanation']
	total_questions = 0
	total_results = 0
	for key in data:
		#this deals with the questions
		if (re.match(r'question\d',key)):
			total_questions = total_questions+1
			question = Question()
			question.question_text = data[key]
			#question.answer1 = data['answer1_q' + str(total_questions)]
			#question.answer2 = data['answer2_q' + str(total_questions)]
			#question.answer3 = data['answer3_q' + str(total_questions)]
			#question.answer4 = data['answer4_q' + str(total_questions)]
			question.QuestionNumber = total_questions
			question.save()
			quiz.questions.add(question)
			quiz.save()
	#we need to change this to deal with variable numbers of answers
	for key in data:
		#this deals with results
		if (re.match(r'r1.*',key)):
			#result scoring is of the form rx_y_z where x is the answer
			#y is the result and z is the question
			result = Result()
			#we need to find the location of result because it could have more than one digit
			left_index = string.find(key,'_')
			right_index = string.rfind(key,'_')
			result_number = key[left_index+1:right_index]
			question_number = key[right_index+1:]
			r_list = Results_List.split(",")
			r_e_list = Results_Explanation_List.split(",")
			result.Quiz_Result = r_list[int(result_number)-1]
			result.Quiz_Result_Explanation = r_e_list[int(result_number)-1]
			scoring_list = []
			for match_key in data:
				if (re.match(r'r1_'+result_number+'.*',match_key)):
					#this takes us through all the scores for a particular results
					result_scoring_list = []
					result_scoring_list.append(data[match_key])
					#we take the end of match_key but replace the begining with r2
					result_scoring_list.append(data['r2'+match_key[2:]])
					result_scoring_list.append(data['r3'+match_key[2:]])
					result_scoring_list.append(data['r4'+match_key[2:]])
					scoring_list.append(result_scoring_list)
			result.Quiz_Scoring = scoring_list
			result.resultNumber = result_number
			result.save()
			#we only add a result for the first question
			if (re.match(r'r1_'+result_number+'_1',key)):
			#right now we're adding this for each question
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
