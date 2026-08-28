from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializer import CatySeriaList,CatySeriaDetail, ProdSeriaList,ProdSeriaDetail,ReviewSeriaDetail,ReviewSeriaList,ProdRevSeriaList

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
    #Homework-3/---------------------------------------->
    if request.method == 'POST':
        name = request.data.get('name')
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
    elif request.method == "PUT":
        caty.name = request.data.get('name')
        caty.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=CatySeriaDetail(caty).data)
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

    #Homework-3/-------------------------------------------------->
    elif request.method == "POST":
        title = request.data.get('title')
        descriptions = request.data.get('descriptions')
        price = request.data.get('price')
        category_id = request.data.get('category_id')

        prod = Product.objects.create(
            title = title,
            descriptions = descriptions,
            price = price,
            category_id = category_id
        )
        return Response(data=ProdSeriaList(prod).data,
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
    elif request.method == "PUT":
        prod.title = request.data.get('title')
        prod.descriptions = request.data.get('descriptions')
        prod.price = request.data.get('price')
        prod.category_id = request.data.get('category')
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
    #Homework-3/------------------------------------------------->
    elif request.method == 'POST':
        text = request.data.get('text')
        product_id = request.data.get('product')
        stars = request.data.get('stars')

        rev = Review.objects.create(
            text=text,
            product_id=product_id,
            stars=stars
        )
        return Response(data=ReviewSeriaList(rev).data,
                        status=status.HTTP_201_CREATED)
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
    elif request.method == 'PUT':
        rev.text = request.data.get('text')
        rev.product_id = request.data.get('product')
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