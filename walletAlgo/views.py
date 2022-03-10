from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
from algosdk.v2client import indexer

def index(request):

    # algod_token = '4xcfeVtFO21zGa5oJr3us3bpzXACJjQg5oPUdTtv'
    # algod_address = 'https://testnet-algorand.api.purestake.io/idx2'
    # purestake_token = {'X-API-Key': algod_token}
    # acl = indexer.IndexerClient(algod_token, algod_address,headers=purestake_token)
    # response = acl.search_transactions(address="JHIBASZEKIAANRRBNU4UTDJ2NLI4ZYRW6UHKHWTTMFUDK7CESTVYC3TEQI")
    # owner="JHIBASZEKIAANRRBNU4UTDJ2NLI4ZYRW6UHKHWTTMFUDK7CESTVYC3TEQI"
    # amt=(response["transactions"])
    # kampy=[]
    # sno=0
    # for amt in amt:
    #   id=amt["id"]
    #   cnfround=amt["confirmed-round"]
    #   amount=amt["payment-transaction"]["amount"]
    #   sender=amt["sender"]
    #   receiver=amt["payment-transaction"]["receiver"]
    #   fee=amt["fee"]
    #   if sender==owner:
    #       tnxtype="Sent"
    #   else:
    #       tnxtype="Receive"
    #   sno=sno+1
    #   divyansh= {"sno":sno,"id":id,"cnfround":cnfround,"amount":amount,"receiver":receiver,"sender":sender ,"fee":fee,"tnxtype":tnxtype}
    #   kampy.append(divyansh)
    #   sno
    # user= get_user_model()
    # if request.method=="POST":
    #     username = request.POST.get('username')
    #     pas = request.POST.get('password')
    #     passfrase = request.POST.get('passfrase')
    #     address = request.POST.get('address')
    #     privatekey = request.POST.get('privatekey')

    #     detail=user.objects.create_user(username=username,password=pas,passfrase=passfrase,Address=address,privateKey=privatekey)
    #     detail.save()

    #     current = str(request.user)
    #     print(current)

    return render(request,'index.html',{'magic':'','name':'Divyansh','bal':'245'})  
      #,{'divyansh':kampy})
# Create your views here.
def login(request):
    # if request.method == "POST":
    #     name = request.POST.get('username')
    #     pwd = request.POST.get('password')
            
    #     user = authenticate(request, username=name,password=pwd)
    #     if user is not None:
    #         login(request,user)
    #         current = str(request.user.username)
    #         print(current)
    #         return redirect("dashboard")
    #     else:
    #         return redirect("divyansh")
            
    return render(request,"login.html")

@login_required(login_url="/login/")
def dashboard(request): 
   
    return render(request,"dashboard.html") 

def recoverAcc(request):
    return render(request,"AddAccount.html")

@login_required(login_url="/login/")
def addacc(request):
    return render(request,"AddAccount2.html")

@login_required(login_url="/login/")
def history(request):
    return render(request,"history.html")

@login_required(login_url="/login/")
def send(request):
    return render(request,"send.html")

@login_required(login_url="/login/")
def recieve(request):
    return render(request,"recieve.html")


def newacc(request):
    return render(request,"NewAccount.html")

def base(request):
    return render(request,"base.html",{'magic':'','name':'name','bal':'245'})
