from rest_framework import serializers
from .models import *

#1-Homework
#Category 
class CatySeriaList(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class  CatySeriaDetail(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

#Product
class ProdSeriaList(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class  ProdSeriaDetail(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

#Review
class ReviewSeriaList(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class  ReviewSeriaDetail(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
