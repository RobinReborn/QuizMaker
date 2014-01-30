from django.db import models
class Quiz(models.Model):
	Quiz_Title = models.CharField(max_length=100)
	Quiz_Description = models.CharField(max_length=1000)
	#each of these is paired to the id of a question
	Quiz_Questions = models.CommaSeparatedIntegerField(max_length=100)

class Question(models.Model):
	question_text = models.CharField(max_length=500)
	answer1 = models.CharField(max_length=50)
	answer2 = models.CharField(max_length=50)
	answer3 = models.CharField(max_length=50)
	answer4 = models.CharField(max_length=50)
	#perhaps I'm getting ahead of myself here
	Answers = ( (answer1, '1'),(answer2, '2'),(answer3,'3'),(answer4,'4'))
	#selectedAnswer = models.CharField(max_length=50,choices=Answers)

	#Quiz_Part = models.ForeignKey(Quiz,default=1)
class Result(models.Model):
	Quiz_Results = models.ForeignKey(Quiz,default=1)
	Quiz_Scoring = models.CommaSeparatedIntegerField(max_length=100)
	Quiz_Result = models.CharField(max_length=100)
	Quiz_Result_Explanation = models.CharField(max_length=1000)
