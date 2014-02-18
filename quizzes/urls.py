
from django.conf.urls import patterns, url

from quizzes import views

urlpatterns = patterns('',
    url(r'^create/created', views.created, name = 'created'),
    url(r'^create/$', views.quiz_create, name='quiz_create'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<Quiz_Name>.+)/$', views.quiz, name='quiz'),
)

