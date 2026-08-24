from rest_framework import serializers
from .models import *
from django.db.models import Avg

#1-Homework
#Category 
class CatySeriaList(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = 'id name product_count'.split()
    #homework-2 --------------------------------->
    def get_product_count(self, category):
        return Product.objects.filter(category=category).count()
    #-------------------------------------------->

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
#-------------------------------------------------------->
#Homework-2

class ProdRevSeriaList(serializers.ModelSerializer):
    review = ReviewSeriaDetail(source='review_set', many=True)
    rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = 'title review rating'.split()

    def get_rating(self,obj):
        average = obj.review_set.aggregate(average=Avg('stars'))['average']
        return average