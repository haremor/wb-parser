from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_products),
    path('products/total/', views.get_total_products),
    path('filters/', views.get_filters)
]