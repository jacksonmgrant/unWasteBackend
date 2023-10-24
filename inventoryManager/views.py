from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the inventory index.")

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer