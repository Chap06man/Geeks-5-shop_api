from django.urls import path
from .  import views

urlpatterns = [
    path('registretion/',views.regstr),
    path('confirm/', views.verify),
    path('login/', views.login)
]