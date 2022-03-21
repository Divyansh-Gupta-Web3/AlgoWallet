from django.contrib import admin
from django.urls import path, include
from walletAlgo import views

urlpatterns = [
      path("",views.index, name='index'),
      path("signin",views.signin, name='signin'),
      path("AddAccount",views.AddAccount, name='AddAcount'),
       path("CreateAccount",views.CreateAccount, name='CreateAccount'),
        path("dashboard",views.dashboard, name='dashboard'),
         path("SendAlgo",views.SendAlgo, name='SendAlgo'),
          path("RecieveAlgo",views.RecieveAlgo, name='RecieveAlgo'),
           path("History",views.History, name='History'),
           path("createRecovery",views.createRecovery, name='createRecovery'),
]
