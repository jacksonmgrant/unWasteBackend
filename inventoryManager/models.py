from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published",default=timezone.now)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    

class Restaurant(models.Model):
	location = models.CharField(max_length=50)
	open_hours = models.IntegerField()
	available_for_pickup = models.DateTimeField()
	cuisine_type = models.CharField(max_length=50) #Chinese, Mexican, Burgers, Pizza, Health Food, Fast Food, etc.

class FoodsInventory(models.Model):
    dietary_restriction = models.CharField(max_length=50) #gluten_free, vegan, low carb, lactose free
    food_name = models.CharField(max_length=50)
    food_description = models.CharField(max_length=500) #restaurant’s description of the food 