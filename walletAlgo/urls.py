from django.contrib import admin
from django.urls import path, include
from walletAlgo import views

urlpatterns = [
    path("",views.index, name='index'),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("signin/",views.divyansh,name="divyansh")
]