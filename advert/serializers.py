from rest_framework import serializers
from .models import Ad, Category

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = ('created', 'updated')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created', 'updated')
