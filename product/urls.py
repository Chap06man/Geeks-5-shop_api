from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.ListCategoryApiViews.as_view()),
    path('category/<int:id>/', views.DetailCategoryApiViews.as_view()),
    path('list/', views.ListProductApiViews.as_view()),
    path('list/<int:id>/', views.DetailProductApiViews.as_view()),
    path('review/', views.ListReviewstApiViews.as_view()),
    path('review/<int:id>/', views.DetailReviewstApiViews.as_view())
]