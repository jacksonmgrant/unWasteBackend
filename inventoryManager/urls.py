from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('api/questions/', views.QuestionList.as_view(), name='question-list'),
    path('api/questions/<int:pk>/', views.QuestionList.as_view(), name='question-detail'),
    path('api/restaurants/', views.RestaurantList.as_view(), name='restaurant-list'),
    path('api/restaurants/<int:pk>/', views.RestaurantList.as_view(), name='restaurant-detail'),
]

#http://192.168.4.24:8080/inventoryManager/api/questions/

#Anna Home IPv4 Restaurant Form
#http://192.168.4.24:8080/inventoryManager/api/restaurants/

#UIowa IPv4 Restaurant Form
#http://172.23.124.194:8080/inventoryManager/api/restaurants/