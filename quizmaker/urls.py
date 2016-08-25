from django.conf.urls import include, url
#from django.conf.urls.defaults import *
from quizzes import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'quizmaker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^quizzes/', include('quizzes.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index, name='index'),

]
