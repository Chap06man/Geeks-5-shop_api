from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import random,time
from . models import LoginTime
@shared_task
def send_otp_mail(email, code):
    send_mail(
        subject="Registration code",
        message=f"your code {code}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )


@shared_task
def send_report_mail():
    send_mail(
        subject="--**",
        message="--",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["sardaryt26@gmail.com"],
    )

@shared_task
def sleep_time_mail():
    send_mail(
        subject="Время !",
        message="Пора спать !?",
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=["sardorbek7@gmail.com"]
    )

@shared_task
def login_static_mail():
    users = LoginTime.objects.all()
    countt = users.count()
    retu = f"Средняя статистика авторизации пользователей: {countt}"

    send_mail(
        subject="Статистика дня",
        message=retu,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["sardorbek7@gmail.com"]
    )

    return retu