from quizzes.models import *
from django.forms import ModelForm

class QuizForm(ModelForm):
	class Meta:
		model = Quiz
		fields = ('Quiz_Title','Quiz_Description','questions')

