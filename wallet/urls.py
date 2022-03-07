from django.contrib import admin
from django.urls import path, include
from wallet import views

urlpatterns = [
    path("",views.index, name='index'),
    path("divyansh/",views.divyansh,name="divyansh")
]