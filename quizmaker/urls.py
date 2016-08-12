from django.conf.urls import include, url
#from django.conf.urls.defaults import *
from quizzes import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'quizmaker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url("",views.index, name='index'),
    url(r'^quizzes/', include('quizzes.urls', namespace="quizzes")),
    url(r'^admin/', include(admin.site.urls)),
]
