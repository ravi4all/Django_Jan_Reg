from django.urls import path
# from .views import HomeView
from . import views

urlpatterns = [
    path(r'',views.index, name='ajax'),
    path(r'login/', views.login, name='login')
]