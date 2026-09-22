from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.ListCategoryApiViews.as_view()),
    path('category/<int:id>/', views.DetailCategoryApiViews.as_view()),
    path(
        'list/',
        views.ProductModelView.as_view({
            'get': 'list',
            'post': 'create',
        })
    ),

    path('<int:pk>/',
        views.ProductModelView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',})),
    #path('list/<int:id>/', views.DetailProductApiViews.as_view()),
    path('review/', views.ListReviewstApiViews.as_view()),
    path('review/<int:id>/', views.DetailReviewstApiViews.as_view())
]