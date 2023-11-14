from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('api/questions/', views.QuestionList.as_view(), name='question-list'),
    path('api/questions/<int:pk>/', views.QuestionList.as_view(), name='question-detail'),
]

#http://192.168.4.24:8080/inventoryManager/api/questions/