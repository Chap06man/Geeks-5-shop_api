from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/categories/',views.list_categories_api_view),
    path('api/v1/categories/<int:id>/', views.deatil_categories_api_view),
    path('api/v1/products/', views.list_product_api_view),
    path('api/v1/products/<int:id>/', views.detail_prod_api_view),
    path('api/v1/reviews/', views.list_review_api_view),
    path('api/v1/reviews/<int:id>/', views.detail_review_api_view),
    path('api/v1/product/reviews/', views.prod_review_list_api_views),
]