from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Question, Restaurant, FoodsInventory
from .serializers import QuestionSerializer, RestaurantSerializer, FoodsInventorySerializer


def index(request):
    return HttpResponse("Hello, world. You're at the inventory index.")

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
class FoodsInventoryList(generics.ListCreateAPIView):
    queryset = FoodsInventory.objects.all()
    serializer_class = FoodsInventorySerializer

class FoodsInventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodsInventory.objects.all()
    serializer_class = FoodsInventorySerializer