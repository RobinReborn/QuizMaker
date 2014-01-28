from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quizmaker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^quizzes/', include('quizzes.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
