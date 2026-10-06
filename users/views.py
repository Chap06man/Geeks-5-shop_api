import random
import redis
from .tasks import send_otp_mail
from django.contrib.auth import authenticate
from django.db import transaction

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser ,LoginTime
from .serializer import (
    AuthValidateSerializer,
    ConfirmationSerializer,
    CustomTokenObtainPairSerializer,
    RegisterValidateSerializer,
)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class AuthorizationAPIView(CreateAPIView):
    serializer_class = AuthValidateSerializer
    def post(self, request):
        serializer = AuthValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)

        if user:
            if not user.is_active:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED,
                    data={"error": "User account is not activated yet!"},)
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={"key": token.key})

        LoginTime.objects.create(user=user)

        return Response(
            status=status.HTTP_401_UNAUTHORIZED,
            data={"error": "User credentials are wrong!"},)

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0
)

class RegistrationAPIView(CreateAPIView):
    serializer_class = RegisterValidateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        with transaction.atomic():
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                is_active=False,
                registration_source="local"
            )

        code = random.randint(100000, 999999)
        send_otp_mail.delay(email, code)

        redis_client.set(
            f"confirmation_code:{user.id}",
            code,
            ex=300
        )

        return Response(
            {
                "message": "Код подтверждения создан",
                "code": code
            },
            status=status.HTTP_201_CREATED
        )


class ConfirmUserAPIView(CreateAPIView):
    serializer_class = ConfirmationSerializer

    def post(self, request):
        serializer = ConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data["user_id"]
        code = serializer.validated_data["code"]

        saved_code = redis_client.get(
            f"confirmation_code:{user_id}"
        )

        if saved_code is None:
            return Response({"error": "Код истёк или не существует"},status=status.HTTP_400_BAD_REQUEST)

        saved_code = saved_code.decode()

        # Проверяем код
        if saved_code != str(code):
            return Response({"error": "Неверный код"},status=status.HTTP_400_BAD_REQUEST)
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "Пользователь не найден"},status=status.HTTP_404_NOT_FOUND)
        with transaction.atomic():
            user.is_active = True
            user.save()

            token, _ = Token.objects.get_or_create(user=user)

        redis_client.delete(f"confirmation_code:{user_id}")
        return Response({"message": "User аккаунт успешно активирован","key": token.key},status=status.HTTP_200_OK)