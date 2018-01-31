from django.urls import path
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

app_name = "twitter"

urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'register/', views.register, name="register"),
    path(r'profile/', views.profile, name="profile"),
    path(r'login/', login, {'template_name' : 'includes/login.html'}, name="login"),
    path(r'logout/', logout, {'template_name' : 'includes/logout.html'}, name="logout")
]