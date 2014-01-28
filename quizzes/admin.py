from django.contrib import admin
from quizzes.models import *
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Result)
# Register your models here.
