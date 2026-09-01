from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializer import CatySeriaList,CatySeriaDetail, ProdSeriaList,ProdSeriaDetail,ReviewSeriaDetail,ReviewSeriaList,ProdRevSeriaList,CatyValidateSerializer,ProductValidateSeriaLizer,ReviewValidateSeria
from django.db import transaction

#1-Homework

#list,Detail - Category 
@api_view(['GET','POST'])
def list_categories_create_api_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        list_ = CatySeriaList(category, many=True).data
        return Response(
            status=status.HTTP_200_OK,
            data = list_
        )
    #Homework-4/---------------------------------------->
    if request.method == 'POST': 
        serializer = CatyValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        name = serializer.validated_data.get('name')
        caty = Category.objects.create(name=name)
        return Response(data=CatySeriaList(caty).data,
                        status=status.HTTP_201_CREATED)
    #--------------------------------------------------->

@api_view(['GET','PUT','DELETE'])
def deatil_categories_api_view(request, id):
    try:
        caty = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error':'Not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)

    #Homework-3/------------------------------------------------>
    if request.method == 'GET':   
        category = Category.objects.get(id=id)
        deatil = CatySeriaDetail(category, many=False).data
        return Response(data=deatil)
    
    elif request.method =='DELETE':
        caty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #homework-4
    elif request.method == "PUT":
        serializer = CatyValidateSerializer(data=request.data)
        if not serializer.is_valid():
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data=serializer.errors)
        name = serializer.validated_data.get('name')
        caty.name = name
        caty.save()
        return Response(data=CatySeriaDetail(caty).data,
                        status=status.HTTP_201_CREATED)
    #-------------------------------------------------------------->

#List,Detail - Product
@api_view(['GET', 'POST'])
def list_product_create_api_view(request):

    if request.method == 'GET':
        product = Product.objects.all()
        list_ = ProdSeriaList(product, many=True).data
        return Response(
            status=status.HTTP_200_OK,
            data=list_
        )

    #Homework-4/-------------------------------------------------->
    elif request.method == "POST":
        serializer = ProductValidateSeriaLizer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        title = serializer.validated_data.get("title")
        descriptions = serializer.validated_data.get("descriptions")
        price = serializer.validated_data.get('price')
        category_id = serializer.validated_data.get('category_id')
        prod_list = Product.objects.create(title=title,
                                           descriptions=descriptions,
                                           price=price,
                                           category_id=category_id
                                           )
        return Response(data=ProdSeriaList(prod_list).data,
                        status=status.HTTP_201_CREATED)
    #-------------------------------------------------------------->

@api_view(['GET','PUT','DELETE'])
def detail_prod_api_view(request, id):
    try:
        prod = Product.objects.get(id=id)
    except Product.DoesNotExist:
           return Response(data={'error':'Not found!!!'},
                           status=status.HTTP_404_NOT_FOUND)

    #Homework-3/-------------------------------------------------->
    if request.method == "GET":
        product = Product.objects.get(id=id)
        deatil = ProdSeriaDetail(product, many=False).data
        return Response(data=deatil) 
    
    elif request.method =='DELETE':
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #Homework-4/-------------------------------------------------->
    elif request.method == "PUT":
        serializer = ProductValidateSeriaLizer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        prod.title = request.data.get('title')
        prod.descriptions = request.data.get('descriptions')
        prod.price = request.data.get('price') 
        prod.category_id = request.data.get('category_id')
        prod.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ProdSeriaDetail(prod).data)   
    #-------------------------------------------------------------------->

#List, Detail - Review
@api_view(['GET','POST'])
def list_review_create_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        list_ = ReviewSeriaList(review, many=True).data
        return Response(
            status=status.HTTP_200_OK,
            data=list_
        )
    #Homework-4/------------------------------------------------->
    elif request.method == 'POST':
        serializer = ReviewValidateSeria(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        text = serializer.validated_data.get('text')
        product_id = serializer.validated_data.get('product_id')
        stars = serializer.validated_data.get('stars')
        review_list = Review.objects.create(text=text,
                                            product_id=product_id,
                                            stars=stars)
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewSeriaList(review_list).data)
    #--------------------------------------------------------------->
        
@api_view(['GET','PUT','DELETE'])
def detail_review_api_view(request, id):
    try:
        rev = Review.objects.get(id=id)
    except Review.DoesNotExist:
           return Response(data={'error':'Not found!!!'},
                           status=status.HTTP_404_NOT_FOUND)
    #Homework-3/------------------------------------------------->
    if request.method == 'GET':
        review = Review.objects.get(id=id)
        deatil = ReviewSeriaDetail(review, many=False).data
        return Response(data=deatil) 
    elif request.method == 'DELETE':
        rev.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #Homework-4/------------------------------------------------->
    elif request.method == 'PUT':
        serializer = ReviewValidateSeria(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        rev.text = request.data.get('text')
        rev.product_id = request.data.get('product_id')
        rev.stars = request.data.get('stars')
        rev.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewSeriaDetail(rev).data)
    #------------------------------------------------------------>

#Homework-2 
@api_view(['GET'])
def prod_review_list_api_views(request):
    prod = Product.objects.all()
    list_ = ProdRevSeriaList(prod,many = True).data
    return Response(status=status.HTTP_200_OK,data=list_)