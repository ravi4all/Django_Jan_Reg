from django.urls import path
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.conf import settings
from django.conf.urls.static import static

app_name = "twitter"

urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'register/', views.register, name="register"),
    path(r'profile/', views.view_profile, name="profile"),
    path(r'edit_profile/', views.edit_profile, name="edit_profile"),
    path(r'login/', login, {'template_name' : 'includes/login.html'}, name="login"),
    path(r'logout/', logout, {'template_name' : 'includes/logout.html'}, name="logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)