from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializer import CatySeriaList, CatySeriaDetail, ProdSeriaList,ProdSeriaDetail,ReviewSeriaDetail,ReviewSeriaList

#1-Homework

#list,Detail - Category 
@api_view(['GET'])
def list_categories_api_view(request):
    category = Category.objects.all()
    list_ = CatySeriaList(category, many=True).data
    return Response(
        status=status.HTTP_200_OK,
        data=list_
    )
@api_view(['GET'])
def deatil_categories_api_view(request, id):
    try:
        caty = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error':'Not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
         
    category = Category.objects.get(id=id)
    deatil = CatySeriaDetail(category, many=False).data
    return Response(data=deatil)

#List,Detail - Product
@api_view(['GET'])
def list_product_api_view(request):
    product = Product.objects.all()
    list_ = ProdSeriaList(product, many=True).data
    return Response(
        status=status.HTTP_200_OK,
        data=list_
    )

@api_view(['GET'])
def detail_prod_api_view(request, id):
    try:
        prod = Product.objects.get(id=id)
    except Product.DoesNotExist:
           return Response(data={'error':'Not found!!!'},
                           status=status.HTTP_404_NOT_FOUND)
    product = Product.objects.get(id=id)
    deatil = ProdSeriaDetail(product, many=False).data
    return Response(data=deatil)      

#List, Detail - Review
@api_view(['GET'])
def list_review_api_view(request):
    review = Review.objects.all()
    list_ = ReviewSeriaList(review, many=True).data
    return Response(
        status=status.HTTP_200_OK,
        data=list_
    )

@api_view(['GET'])
def detail_review_api_view(request, id):
    try:
        rev = Review.objects.get(id=id)
    except Review.DoesNotExist:
           return Response(data={'error':'Not found!!!'},
                           status=status.HTTP_404_NOT_FOUND)
    review = Review.objects.get(id=id)
    deatil = ReviewSeriaDetail(review, many=False).data
    return Response(data=deatil) 