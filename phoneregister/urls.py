from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.phone_login, name='phone_login'),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('verify/', views.verify, name='verify'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
