from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random
from . models import VerifyCodeModel

from rest_framework.views import APIView

from .serializer import (
    UserCreateSerializer,
    UserAuthSerializer,
    VerifyCodeValid
    )

#<-------------------------------------------------------------------------------------------------------------->

#class for registration 
class RegisterView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.create_user(username=username,password=password)

        user.is_active = False
        user.save()
        code = random.randint(100000, 999999)
        VerifyCodeModel.objects.create(user=user,code=code)
        return Response({"message": "Код подтверждения создан"})

#class for confirm
class ConfirmView(APIView):

    def post(self, request):
        username = request.data.get('username')
        code = request.data.get('code')
        user = User.objects.get(username=username)
        verify_code = VerifyCodeModel.objects.get(user=user)
        if verify_code.code == int(code):
            user.is_active = True
            user.save()
            return Response({"message": "Пользователь подтверждён"})
        return Response({"error": "Неверный код"})
    
#class for login 
class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,password=password)
        if user is None:
            return Response({"error": "Неверный логин или пароль"})
        if not user.is_active:
            return Response({"error": "Пользователь не подтверждён"})
        return Response({"message": "Авторизация успешна"})


#registration
# @api_view(['GET','POST'])
# def regstr(request):
#     serializer = UserCreateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)

#     username = request.data.get('username')
#     password = request.data.get('password')

#     user = User.objects.create_user(
#         username=username,
#         password=password,
#         is_active=False
#     )
#     code = random.randint(100000,999999)
#     VerifyCodeModel.objects.create(
#         user = user,
#         code =(code)
#     )
#     return Response(status=status.HTTP_201_CREATED,
#                     data={'user_id': user.id, 'code':code})

# @api_view(['POST'])
# def verify(request):
#     serializer = VerifyCodeValid(data=request.data)
#     serializer.is_valid(raise_exception=True)

#     username = serializer.validated_data.get('username')
#     code = serializer.validated_data.get('code')

#     user = User.objects.get(username=username)
#     confirm = VerifyCodeModel.objects.get(user=user)

#     if confirm.code == code:
#         user.is_active = True
#         user.save()

#         confirm.delete()

#         return Response({'detail': 'Confirm success'})

#     return Response(
#         {'detail': 'Code does not exist'},
#         status=status.HTTP_400_BAD_REQUEST
#     )

# @api_view(['POST'])
# def login(request):
#     serializer = UserAuthSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)

#     user = authenticate(**serializer.validated_data)  # user / None
#     if user:
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response(data={'key': token.key})
#     return Response(status=status.HTTP_401_UNAUTHORIZED)