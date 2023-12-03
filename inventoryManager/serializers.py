from rest_framework import serializers
from .models import Question, Restaurant, FoodsInventory

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
        
class FoodsInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodsInventory
        fields = '__all__'