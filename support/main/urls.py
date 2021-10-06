from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('user', views.user),
    path('support', views.support),
    path('create_user/', views.create_user),
    path('create_support/', views.create_support)
]
