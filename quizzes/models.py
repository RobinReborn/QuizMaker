from django.db import models
class Quiz(models.Model):
	Quiz_Title = models.CharField(max_length=100)
	Quiz_Description = models.CharField(max_length=1000)
	#each of these is paired to the id of a question
	questions = models.ManyToManyField('Question', null=True, blank=True)
	#Quiz_Questions = models.CommaSeparatedIntegerField(max_length=100)
	results = models.ManyToManyField('Result', null=True, blank=True)
	image = models.ImageField(Quiz_Title,100,100)
	date = models.DateTimeField(auto_now=True)
	timesTaken = models.IntegerField()
	def __unicode__(self):
		        return unicode(self.questions)
	
class Question(models.Model):
	question_text = models.CharField(max_length=500)
	num_answers = models.IntegerField()
	questionNumber = models.IntegerField()
	#this should place the image in quiz/question_pk
	image = models.ImageField(Quiz.objects.get(questions=self) + '/' + self.pk)

class Answer(models.Model):
	question = models.ForeignKey('Question',null=True,blank=True)
	answertext = models.CharField(max_length=100)
	#this should place the image in quiz/question_pk/answer_pk
	image = models.ImageField(Quiz.objects.get(questions=question) + '/' + question.pk + '/' + Answer.pk)
	def __unicode__(self):
		        return unicode(self.question_text)
	#Quiz_Part = models.ForeignKey(Quiz,default=1)
class Result(models.Model):
	#Quiz_Results = models.ForeignKey(Quiz,default=1)
	Quiz_Scoring = models.CommaSeparatedIntegerField(max_length=100)
	Quiz_Result = models.CharField(max_length=100)
	resultNumber = models.IntegerField()
	def __unicode__(self):
		        return unicode(self.Quiz_Result)
	Quiz_Result_Explanation = models.CharField(max_length=1000)
	image = models.ImageField(Quiz.objects.get(results=self) + '/' + Quiz_Result)
