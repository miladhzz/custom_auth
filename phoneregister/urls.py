from django.urls import path
from . import views


urlpatterns = [
    path('', views.signup, name='signup'),
    path('verify/', views.verify, name='verify'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.log_out, name='logout'),
]
