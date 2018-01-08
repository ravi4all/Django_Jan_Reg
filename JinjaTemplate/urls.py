# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'products/', views.products, name='products'),
    path(r'cart/', views.cart, name='cart'),
]