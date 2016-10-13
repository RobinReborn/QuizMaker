from django.shortcuts import render
from django.http import HttpResponse
from quizzes.models import *
from django.template import RequestContext, loader, Template
from django.views.decorators.csrf import csrf_protect
from django.views.decorators import csrf

from django.shortcuts import render_to_response
import re
import string
from django.http import QueryDict
from django.template.loader import get_template


def index(request):
	quiz_list = Quiz.objects.all()
	context = {'quiz_list': quiz_list}
	return render(request, 'quizzes/index.html', context)
def quiz(request,Quiz_Name):
	quiz_request = Quiz.objects.get(Quiz_Title=Quiz_Name)
	quiz_questions = []
	quiz_answers = []
	for q in Question.objects.filter(quiz=quiz_request).order_by('questionNumber'):
		if (q != ','):
			quiz_questions.append(q)
			for a in Answer.objects.filter(question=q).order_by('answerNumber'):
				quiz_answers.append(a)
	template = loader.get_template('quizzes/quiz.html')
	context = {'quiz_request': quiz_request, 'quiz_questions': quiz_questions, 'quiz_answers': quiz_answers}
	return render(request, 'quizzes/quiz.html', context)  
def result(request,Quiz_Name):
	data = request.POST.dict()
	correctAnswers = 0
	quiz_questions = []
	quiz_answers = []
	correctAnswerArray = []
	compareAnswerArray = []
	userAnswerArray = []
	quiz = Quiz.objects.get(Quiz_Title=Quiz_Name)
	for q in Question.objects.filter(quiz=quiz).order_by('questionNumber'):
		if (q != ','):
			quiz_questions.append(q)
			for a in Answer.objects.filter(question=q).order_by('answerNumber'):
				quiz_answers.append(a)
	#here we go through all the questions, find the correct answer and see if that matches the user input
	for z in range(1,quiz.question_set.count()+1):
		q = quiz.question_set.get(questionNumber=z)
		correctAnswer = q.answer_set.get(correctAnswer="True").answerNumber
		correctAnswerArray.append(int(correctAnswer))
		userAnswerArray.append(int(data["question-"+str(z)]))
		#if (int(data["question-"+str(z)]) == correctAnswer):
		#	correctAnswers = correctAnswers+1
		#	correctAnswerArray.append("1")
		#else:
		#	correctAnswerArray.append("0")
	compareAnswerArray = zip(correctAnswerArray,userAnswerArray)
	print compareAnswerArray	
	c = {'correctAnswers' : correctAnswers,'quiz_questions': quiz_questions, 'quiz_answers': quiz_answers, 'compareAnswerArray': compareAnswerArray}
	template = loader.get_template('quizzes/result.html')
	return render(request,'quizzes/result.html',c)
def quiz_create(request):
	c = {'request' : request}
	template = loader.get_template('quizzes/quiz_create.html')
	return render(request,"quizzes/quiz_create.html", c)
def add_answers(request):	
	template = loader.get_template('quizzes/quiz_create.html')
	data = request.POST.dict()
	quiz = Quiz()
	quiz.Quiz_Title = request.POST['Quiz_Name']
	quiz.Quiz_Description = request.POST['Quiz_Description']
	quiz.save()
	QuestionArray = data["questionArray"].split(",")
	#we create a question for each question in teh array
	for x in range(0, len(QuestionArray)):
		question = Question()
		question.question_text = QuestionArray[x]
		question.questionNumber = x+1
		question.save()
		quiz.question_set.add(question)
	quiz.save()
	context = {'Quiz_Name': data['Quiz_Name'], 'Quiz_Description': data['Quiz_Description'], 'questions' : QuestionArray}
	return render(request,"quizzes/add_answers.html", context)
def add_results(request):
	data= request.POST.dict()
	questionArray = data['Questions']
	#first we split up each set of answers
	answerArray = data['AnswersArray'].split(",/,")
	#then we split up the individual answers
	for x in range(0,len(answerArray)):
		answerArray[x] = answerArray[x].split(",")
	#we need to get rid of the last element in the array because of the way things are split
	del answerArray[-1][-1]
	quiz = Quiz.objects.get(Quiz_Title=data['Quiz_Name'])
	quizType = data['quizType']	
	for x in range(0,len(answerArray)):
		correctAnswer = int(answerArray[x][0])
		#we delete the index of the correct answer as we do not create an object for it
		del answerArray[x][0]
		questionNumber = x+1
		question_add = quiz.question_set.get(questionNumber=questionNumber)
		for a in range(0,len(answerArray[x])):
			#for each answer we add information, then add it to the appropriate question
			answer = Answer()
			if (a == correctAnswer):
				answer.correctAnswer = "True"
			else:
				answer.correctAnswer = "False"
			answer.answertext = answerArray[x][a]
			answer.answerNumber = a+1
			answer.save()
			question_add.answer_set.add(answer)
		question_add.save()
	quiz.save()
	context = {'quizType': quizType, 'quiz': quiz}
	return render(request,'quizzes/add_results.html',context)
def created(request):
	print "in created"
	data = request.POST.dict()
	template = loader.get_template('quizzes/quiz_created.html')
    #here we do some stuff to add the quiz, questions and results to our DB
	quiz = Quiz()
	quiz.Quiz_Title = request.POST['Quiz_Name']
	quiz.Quiz_Description = request.POST['Quiz_Description']
	quiz.save()
	total_questions = int(data['numQuestions'])
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
