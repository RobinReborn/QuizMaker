from django.db import models
class Quiz(models.Model):
	DEFAULT_PK =1
	Quiz_Title = models.CharField(max_length=100)
	Quiz_Description = models.CharField(max_length=1000)
	#each of these is paired to a question
	#questions = models.ManyToManyField('Question', blank=True)
	results = models.ManyToManyField('Result', blank=True)
	image = models.ImageField(upload_to='/images/',default=None)
	date = models.DateTimeField(auto_now=True)
	timesTaken = models.IntegerField(default=0)
	Quiz_Type = models.CharField(max_length=1000)
	def __unicode__(self):
		return unicode(self.Quiz_Title)
class Question(models.Model):
	DEFAULT_PK=1
	quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,default=Quiz.DEFAULT_PK)
	question_text = models.CharField(max_length=500)
	num_answers = models.IntegerField(default=0)
	questionNumber = models.IntegerField(default=0)
	#image = models.ImageField(upload_to='/images/',default=None)
	#answers = models.ManyToManyField('Answer',blank=True)
	def __unicode__(self):
		return unicode(self.question_text)
	def sortAnswers(self):
		return self.answers.all().order_by('answerNumber')
class Answer(models.Model):
	#question = models.ForeignKey('Question',null=True,blank=True)
	question = models.ForeignKey(Question,on_delete=models.CASCADE,default=Question.DEFAULT_PK)
	answertext = models.CharField(max_length=100)
	answerNumber = models.IntegerField(default=0)
	correctAnswer = models.CharField(max_length=20,default=None)
	def __unicode__(self):
		return unicode(self.answertext)
	#Quiz_Part = models.ForeignKey(Quiz,default=1)
class Result(models.Model):
	#Quiz_Results = models.ForeignKey(Quiz,default=1)
	#this will need to change to allow for easy scoring
	Quiz_Scoring = models.CharField(max_length=100)
	Quiz_Result = models.CharField(max_length=100)
	resultNumber = models.IntegerField()
	def __unicode__(self):
		        return unicode(self.Quiz_Result)
	Quiz_Result_Explanation = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='/images/',default=None)
