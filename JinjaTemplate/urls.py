# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'products/', views.products, name='products'),
    path(r'cart/', views.cart, name='cart'),
    path(r'contact/', views.contact, name='contact'),
    path(r'sortByPrice/', views.sortByPrice, name='sortByPrice'),
    path(r'searchProduct/', views.searchProduct, name='searchProduct'),
]