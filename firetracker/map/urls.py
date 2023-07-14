
from django.contrib import admin
from django.urls import path,include
from map import views

urlpatterns = [

    path('', views.index),
]
