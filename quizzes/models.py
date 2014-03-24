from django.db import models
class Quiz(models.Model):
	Quiz_Title = models.CharField(max_length=100)
	Quiz_Description = models.CharField(max_length=1000)
	#each of these is paired to a question
	questions = models.ManyToManyField('Question', null=True, blank=True)
	results = models.ManyToManyField('Result', null=True, blank=True)
	image = models.ImageField(upload_to='/images/')
	date = models.DateTimeField(auto_now=True)
	timesTaken = models.IntegerField(default=0)
	Quiz_Type = models.CharField(max_length=1000)
	def __unicode__(self):
		return unicode(self.questions)
	
class Question(models.Model):
	question_text = models.CharField(max_length=500)
	num_answers = models.IntegerField(default=0)
	questionNumber = models.IntegerField(default=0)
	#this should place the image in quiz/question_pk
	#def imageLocation(self):
	#	return Quiz.objects.get(questions=self) + '/' + self.pk
	image = models.ImageField(upload_to='/images/')

class Answer(models.Model):
	question = models.ForeignKey('Question',null=True,blank=True)
	answertext = models.CharField(max_length=100)
	#this should place the image in quiz/question_pk/answer_pk
	image = models.ImageField(upload_to='/images/')
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
	image = models.ImageField(upload_to='/images/')
