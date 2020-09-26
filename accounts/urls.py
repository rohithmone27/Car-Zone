from django.urls import path
from . import views

urlpatterns = [
    path('logon', views.logon, name='logon'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]