

from django.conf.urls import url
from quizzes import views

urlpatterns = [
    url(r'^create/created', views.created, name = 'created'),
    url(r'^create/$', views.quiz_create, name='quiz_create'),
    url(r'', views.index, name='index'),
	url(r'^(?P<Quiz_Name>.+)/result', views.result, name='result'),
	url(r'^(?P<Quiz_Name>.+)/$', views.quiz, name='quiz'),
]

