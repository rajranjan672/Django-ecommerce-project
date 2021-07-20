from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customers, name='customer'),

    path('create_order/<str:pk>/', views.createOrder),
    path('update_order/<str:pk>/', views.updateOrder),
    path('delete/<str:pk>/', views.deleteOrder),

]