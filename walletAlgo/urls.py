from django.contrib import admin
from django.urls import path, include
from walletAlgo import views

urlpatterns = [
    path("",views.index, name='index'),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("login/",views.login,name="login"),
    path("recoverAcc/",views.recoverAcc,name="recoverAcc"),
    path("addacc/",views.addacc,name="addacc"),
    path("send/",views.send,name="send"),
    path("recieve/",views.recieve,name="recieve"),
    path("newacc/",views.newacc,name="newacc"),
    path("history/",views.history,name="history"),


]
