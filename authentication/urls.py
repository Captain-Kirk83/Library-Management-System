from django.urls import path
from django.contrib.auth import views as auth_views
from authentication.views import *

urlpatterns = [
    path('accounts/login/',loginView, name='login'),
    path('accounts/logout/',logoutView, name='logout'),
    path('accounts/register/',registerView, name='register'),
]