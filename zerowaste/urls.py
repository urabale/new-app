from unicodedata import name
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from . import views

app_name = 'zerowaste'

urlpatterns = [
    path('index', views.ListView.as_view(), name='index'),
    path('add/', views.CreateView.as_view(), name='add'),
    path('create_account/', views.create_account, name='create_account'), 
    path('', views.Login_account.as_view(), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path("password_reset", views.password_reset_request, name="password_reset")
] 