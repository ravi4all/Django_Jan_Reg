from django.urls import path
from . import views
from django.contrib.auth.views import login

app_name = "twitter"

urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'login/', login, {'template_name' : 'includes/login.html'}, name="login")
]