from django.contrib import admin

from .models import Question, Restaurant, FoodsInventory

admin.site.register(Question)

admin.site.register(Restaurant)

admin.site.register(FoodsInventory)