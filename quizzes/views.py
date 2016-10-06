from django.shortcuts import render
from django.http import HttpResponse
from quizzes.models import *
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators import csrf

from django.shortcuts import render_to_response
import re
import string
#from helper_functions import process_Quiz
from django.http import QueryDict
#from django.template.context_processors import csrf
#from django.template import Context
from django.template.loader import get_template
from django.template import Template, RequestContext


def index(request):
	print "in index"
	quiz_list = Quiz.objects.all()
	#template = loader.get_template('quizzes/index.html')
	context = {'quiz_list': quiz_list}
	#return render(request, 'quizzes/index.html', context)
	#template = get_template('quizzes/index.html')
	return render(request, 'quizzes/index.html', context)
#@csrf_protect
def quiz(request,Quiz_Name):
	quiz_request = Quiz.objects.get(Quiz_Title=Quiz_Name)
	quiz_questions = []
	quiz_answers = []
	quiz_results = []
	for q in quiz_request.questions.all().order_by('questionNumber'):
		if (q != ','):
			quiz_questions.append(q)
			#right now we're going through all the answers
			#we could change the model to have answers belong to questions
			#rather than the other way around
			for a in Answer.objects.filter(question=q).order_by('answerNumber'):
				quiz_answers.append(a)
	for r in quiz_request.results.all().order_by('resultNumber'):
		if (r != ','):
			quiz_results.append(r)
	template = loader.get_template('quizzes/quiz.html')
	context = {'quiz_request': quiz_request, 'quiz_questions': quiz_questions, 'quiz_answers': quiz_answers, 'quiz_results': quiz_results}
	return render(request, 'quizzes/quiz.html', context)  

#@csrf_protect
def quiz_create(request):
	#print "in quiz create"
	c = {'request' : request}
	#print "in quiz create \n"
	#c.update(csrf(request))
	#print c
	template = loader.get_template('quizzes/quiz_create.html')
    #return render(request,'quizzes/quiz_create.html')print c
	return render(request,"quizzes/quiz_create.html", c)
def add_answers(request):	
	template = loader.get_template('quizzes/quiz_create.html')
	data = request.POST.dict()
	#questions = []
	QuestionArray = data["questionArray"].split(",")
	quiz = Quiz()
	quiz.Quiz_Title = request.POST['Quiz_Name']
	quiz.Quiz_Description = request.POST['Quiz_Description']
	quiz.save()
	for x in range(0, len(QuestionArray)):
		#print str(x+1)+ QuestionArray[x] + "\n"
		#questions.append(data[key])
		question = Question()
		question.question_text = QuestionArray[x]
		question.questionNumber = x+1
		question.save()
		quiz.question_set.add(question)
		#quiz.questions.add(question)
		quiz.save()
		#print "\n added q" + question.questionNumber
	quiz.save()
	context = {'Quiz_Name': data['Quiz_Name'], 'Quiz_Description': data['Quiz_Description'], 'questions' : QuestionArray}
	return render(request,"quizzes/add_answers.html", context)
def add_results(request):
	data= request.POST.dict()
	dataList = []
	questionArray = data['Questions']
	questionsArray = data['Questions']
	quiz = Quiz.objects.get(Quiz_Title=data['Quiz_Name'])
	quizType = data['quizType']
	if ('scoringType' in data):
		quizType += '/' + data['scoringType']
	for key in data:
		if (re.match(r'q\d+a\d+',key)):
			answerIndex = re.findall(r'\d+',key)
			answer = Answer()
			question_number = int(answerIndex[0])
			answer.answerNumber = answerIndex[1]
			answer.answertext = data[key]
			correctAnswer = data["q" + answerIndex[0] + "a"]
			if (answerIndex[1]== correctAnswer):
				answer.correctAnswer = "True"
			else:
				answer.correctAnswer = "False"
			answer.save()
			question_add = quiz.question_set.get(questionNumber=question_number)
			question_add.answer_set.add(answer)
			question_add.save()
			#question_add.answers.order_by(answerNumber)
		dataList.append({data[key],key})
	context = {'data': dataList, 'quizType': quizType, 'quiz': quiz}
	return render(request,'quizzes/add_results.html',context)
#@csrf_protect
def result(request,Quiz_Name):
	quiz = Quiz.objects.get(Quiz_Title=Quiz_Name)
	results = []
	quiz.results.order_by('resultNumber','id')
	quiz.save()
	for r in quiz.results.all():
		if (r != ','):
			results.append(r)
			print r.resultNumber
	c = {'request' : request, 'results' : results}
	c.update(csrf(request))
	template = loader.get_template('quizzes/result.html')
	#print results
	return render(request,'quizzes/result.html',c)
#@csrf_protect
def created(request):
	print "in created"
	data = request.POST.dict()
	template = loader.get_template('quizzes/quiz_created.html')
    #here we do some stuff to add the quiz, questions and results to our DB
	quiz = Quiz()
	quiz.Quiz_Title = request.POST['Quiz_Name']
	quiz.Quiz_Description = request.POST['Quiz_Description']
	quiz.save()
	#Results_List = data['All_Results']
	#Results_Explanation_List = data['All_Results_Explanation']
	#questionAnswersArray = data['questionAnswersArray']
	#q_a_a_list = questionAnswersArray.split(",")
	#r_list = Results_List.split(",")
	#r_e_list = Results_Explanation_List.split(",")
	total_questions = int(data['numQuestions'])
	#total_results = int(data['numResults'])
	#questions =1
	#for key in data:
		#this deals with the questions
		
	#	if (re.match(r'question\d',key)):
	#		question = Question()
	#		question.question_text = data[key]
	#		question.questionNumber = questions
	#		question.num_Answers = q_a_a_list[questions-1]
	#		question.save()
	#		quiz.questions.add(question)
	#		questions = questions+1
	quiz.save()
	#for key in data:
		#this deals with answers
	#	if (re.match(r'answer.*',key)):
	#		answer = Answer()
	#		answer.answertext = data[key]
			#print data[key]
			#we parse the key to find the question and answer number
	#		answerNumber = key[6:string.find(key,'_')]
	#		questionNumber = key[string.find(key,'_') + 2:]
	#		answer.answerNumber = answerNumber
	#		#maybe not the most efficient way of doing this
	#		question_add = quiz.questions.get(questionNumber=questionNumber)
	#		answer.save()
	#		question_add.answers.add(answer)
	#		question_add.save()
			#question_add.answers.order_by(answerNumber)
	#we need to order the answers
	#result_number = 0
	#for x in range(1,total_results+1):
	#	quiz_scoring = []
	#	result = Result()
	#	result.Quiz_Result = r_list[x-1]
	#	print r_list[x-1]
	#	result.Quiz_Result_Explanation = r_e_list[x-1]
	#	for y in range(1,total_questions+1):
	#		score_list = []
	#		for z in range(0,(int(q_a_a_list[y]) )):
	#			score_list.append(data['r'+str(y)+'_'+str(x)+'_'+str(z+1)])
	#		quiz_scoring.append(score_list)
	#	result.Quiz_Scoring = quiz_scoring
	#	result.resultNumber = x
		#result.Quiz_Result = 
	#	result.save()
	#	print result.Quiz_Result
	#	quiz.results.add(result)
	#	quiz.save()
	#for key in data:
	#	result_scoring_list=[]
	#	total_scoring_list=[]
	#	result = Result()
		#we can rely in having a score value for r1_y_z, then look through y and z
	#	if (re.match(r'r1.*',key)):
			#result scoring is of the form rx_y_z where x is the answer
			#y is the result and z is the question
	#		result = Result()
			#we need to find the location of result because it could have more than one digit
	#		left_index = string.find(key,'_')
	#		right_index = string.rfind(key,'_')
	#		result_number = key[left_index+1:right_index]
	#		question_number = key[right_index+1:]
	#		result.Quiz_Result = r_list[int(result_number)-1]
	#		result.Quiz_Result_Explanation = r_e_list[int(result_number)-1]
			#total_scoring_list = []
			#this deals with a specific answer in the results
			#right now the scoring list doesn't contain all the information it needs to
			#for match_key in data:
			#if (re.match(r'r1_'+result_number+'.*',match_key)):
			#this takes us through all the scores for a particular results
	#		result_scoring_list = []
			#result_scoring_list.append(data[match_key])
			#for each answer in the question
	#		for x in range(0,(int(q_a_a_list[int(question_number)]) )):
				#print x
	#			print "appending to" + question_number
	#			print 'r'+str(x+1)+key[left_index:]
	#			print data['r'+str(x+1)+'_'+result_number+'_'+question_number]
	#			result_scoring_list.append(data['r'+str(x+1)+'_'+result_number+'_'+question_number])
	#		total_scoring_list.append(result_scoring_list)
	#		result.Quiz_Scoring = total_scoring_list
		#print result_number
		#print total_scoring_list
	#		result_number = int(result_number)
	#		result.resultNumber = result_number
	#		result.save()
	#		result_number = result_number+1
		#this needs to be modified
		#we only add a result for the first question
		#if (re.match(r'r1_'+result_number+'_1',key)):
		#right now we're adding this for each question
	#		quiz.results.add(result)
	#		print "saving result"
	#		print result.resultNumber
	#		print result.Quiz_Scoring
	#		quiz.save()
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
