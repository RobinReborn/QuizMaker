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
	quiz_answers = []
	for q in quiz_request.questions.all():
		if (q != ','):
			quiz_questions.append(q)
			#right now we're going through all the answers
			#we could change the model to have answers belong to questions
			#rather than the other way around
			for a in Answer.objects.filter(question=q):
				quiz_answers.append(a)
	template = loader.get_template('quizzes/quiz.html')
	context = {'quiz_request': quiz_request, 'quiz_questions': quiz_questions, 'quiz_answers': quiz_answers}
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
	questionAnswersArray = data['questionAnswersArray']
	q_a_a_list = questionAnswersArray.split(",")
	r_list = Results_List.split(",")
	r_e_list = Results_Explanation_List.split(",")
	total_questions = 0
	total_results = 0
	for key in data:
		#this deals with the questions
		if (re.match(r'question\d',key)):
			total_questions = total_questions+1
			question = Question()
			question.question_text = data[key]
			question.questionNumber = total_questions
			question.num_Answers = q_a_a_list[total_questions]
			question.save()
			quiz.questions.add(question)
			quiz.save()
	for key in data:
		#this deals with answers
		if (re.match(r'answer.*',key)):
			answer = Answer()
			answer.answer_text = data[key]
			#we parse the key to find the question and answer number
			answerNumber = key[6:string.find(key,'_')]
			questionNumber = key[string.find(key,'_') + 2:]
			answer.answerNumber = answerNumber
			question_add = quiz.questions.get(questionNumber=questionNumber)
			answer.save()
			question_add.add(answer)
	#we need to change this to deal with variable numbers of answers
	for key in data:
		#we can rely in having a score value for r1_y_z, then look through y and z
		if (re.match(r'r1.*',key)):
			#result scoring is of the form rx_y_z where x is the answer
			#y is the result and z is the question
			result = Result()
			#we need to find the location of result because it could have more than one digit
			left_index = string.find(key,'_')
			right_index = string.rfind(key,'_')
			result_number = key[left_index+1:right_index]
			question_number = key[right_index+1:]
			result.Quiz_Result = r_list[int(result_number)-1]
			result.Quiz_Result_Explanation = r_e_list[int(result_number)-1]
			total_scoring_list = []
			#this deals with a specific answer in the results
			for match_key in data:
				if (re.match(r'r1_'+result_number+'.*',match_key)):
					#this takes us through all the scores for a particular results
					result_scoring_list = []
					result_scoring_list.append(data[match_key])
					#for each question
					for x in range(1,(int(q_a_a_list[int(question_number)])-1 )):
						#print x
						#print match_key
						result_scoring_list.append(data['r'+str(x)+ match_key[left_index:]])
					#result_scoring_list.append(data['r3'+match_key[2:]])
					#result_scoring_list.append(data['r4'+match_key[2:]])
					total_scoring_list.append(result_scoring_list)
			result.Quiz_Scoring = total_scoring_list
			result.resultNumber = result_number
			result.save()

			#this needs to be modified
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
