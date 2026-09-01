from rest_framework import serializers
from .models import *
from django.db.models import Avg
from rest_framework.exceptions import ValidationError

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

#Homework-4/--------------------------------------------------------------------->

#for Categories
class CatyValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=25, min_length=1)
    def validate_name(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError('name должен быть строкой')
        return value
#for product
class ProductValidateSeriaLizer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=25, min_length=1)
    descriptions = serializers.CharField(required=False, max_length=25, min_length=1)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()
    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category not found!')
        return category_id

#for  Review 
class ReviewValidateSeria(serializers.Serializer):
    text = serializers.CharField(required = True, max_length=55)
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField(required=True)

    def validate_stars(self, stars):
        if stars < 1 or stars > 5:
            raise ValidationError('Stars должно быть от 1 до 5')
        return stars

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except:
            raise ValidationError('Product not found!')
        return product_id
    