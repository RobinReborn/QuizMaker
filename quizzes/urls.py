
from django.conf.urls import patterns, url

from quizzes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

