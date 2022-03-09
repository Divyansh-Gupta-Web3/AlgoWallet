from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
import json
from algosdk.v2client import indexer

def index(request):

    algod_token = '4xcfeVtFO21zGa5oJr3us3bpzXACJjQg5oPUdTtv'
    algod_address = 'https://testnet-algorand.api.purestake.io/idx2'
    purestake_token = {'X-API-Key': algod_token}
    acl = indexer.IndexerClient(algod_token, algod_address,headers=purestake_token)
    response = acl.search_transactions(address="JHIBASZEKIAANRRBNU4UTDJ2NLI4ZYRW6UHKHWTTMFUDK7CESTVYC3TEQI")
    owner="JHIBASZEKIAANRRBNU4UTDJ2NLI4ZYRW6UHKHWTTMFUDK7CESTVYC3TEQI"
    amt=(response["transactions"])
    kampy=[]
    sno=0
    for amt in amt:
      id=amt["id"]
      cnfround=amt["confirmed-round"]
      amount=amt["payment-transaction"]["amount"]
      sender=amt["sender"]
      receiver=amt["payment-transaction"]["receiver"]
      fee=amt["fee"]
      if sender==owner:
          tnxtype="Sent"
      else:
          tnxtype="Receive"
      sno=sno+1
      divyansh= {"sno":sno,"id":id,"cnfround":cnfround,"amount":amount,"receiver":receiver,"sender":sender ,"fee":fee,"tnxtype":tnxtype}
      kampy.append(divyansh)
      sno
    # user= get_user_model()
    # if request.method=="POST":
    #     username = request.POST.get('username')
    #     pas = request.POST.get('password')
    #     passfrase = request.POST.get('passfrase')
    #     address = request.POST.get('address')
    #     privatekey = request.POST.get('username')

    #     detail=user.objects.create_user(username=username,password=pas,passfrase=passfrase,Address=address,privateKey=privatekey)
    #     detail.save()

    #     current = str(request.user)
    #     print(current)

    return render(request,'test.html',{'divyansh':kampy})
# Create your views here.
def divyansh(request):
    if request.method == "POST":
        name = request.POST.get('username')
        pwd = request.POST.get('password')
            
        user = authenticate(request, username=name,password=pwd)
        if user is not None:
            login(request,user)
            current = str(request.user.Address)
            print(current)
            return redirect("index")
        else:
            return redirect("divyansh")
            

    return render(request,"divyansh.html")

def dashboard(request): 
    params={"name":"Divyansh","bal":"SJCNSDCJASIOCNAOSICNASIONCOASNC"}
    return render(request,"dashboard.html",params) 