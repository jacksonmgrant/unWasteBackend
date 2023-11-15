from django.contrib import admin

from .models import Question, Restaurant

admin.site.register(Question)

admin.site.register(Restaurant)