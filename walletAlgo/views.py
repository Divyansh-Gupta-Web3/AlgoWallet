from pprint import pprint
from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
from algosdk.v2client import indexer
from algosdk import mnemonic

passphrase=[]

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
def signin(request):
    if request.method == "POST":
        name = request.POST.get('username')
        pwd = request.POST.get('password')
            
        user = authenticate(request, username=name,password=pwd)
        if user is not None:
            login(request,user)
            current = str(request.user.username)
            print(current)
            return redirect("dashboard")
        else:
            return redirect("signin")
            
    return render(request,"login.html")

@login_required(login_url="/signin/")
def dashboard(request): 
   
    return render(request,"dashboard.html") 

def recoverAcc(request):
    if request.method=="POST":
        p1 = request.POST.get('p1')
        p2 = request.POST.get('p2')
        p3 = request.POST.get('p3')
        p4 = request.POST.get('p4')
        p5 = request.POST.get('p5')
        p6 = request.POST.get('p6')
        p7 = request.POST.get('p7')
        p8 = request.POST.get('p8')
        p9 = request.POST.get('p9')
        p10 = request.POST.get('p10')
        p11 = request.POST.get('p11')
        p12 = request.POST.get('p12')
        p13 = request.POST.get('p13')
        p14 = request.POST.get('p14')
        p15 = request.POST.get('p15')
        p16 = request.POST.get('p16')
        p17 = request.POST.get('p17')
        p18 = request.POST.get('p18')
        p19 = request.POST.get('p19')
        p20 = request.POST.get('p20')
        p21 = request.POST.get('p21')
        p22 = request.POST.get('p22')
        p23 = request.POST.get('p23')
        p24 = request.POST.get('p24')
        p25 = request.POST.get('p25')
    
        passphrase = f'{p1} {p2} {p3} {p4} {p5} {p6} {p7} {p8} {p9} {p10} {p11} {p12} {p13} {p14} {p15} {p16} {p17} {p18} {p19} {p20} {p21} {p22} {p23} {p24} {p25}'
        print(passphrase)
        mnemonic_phrase = passphrase
        account_private_key = mnemonic.to_private_key(mnemonic_phrase)
        account_public_key = mnemonic.to_public_key(mnemonic_phrase)
        memo=passphrase
        privatekey=account_private_key
        address=account_public_key
        print(passphrase)
        print("your account recovered and your address is "+account_public_key + '\n'+ "and your private key is "+account_private_key)
        recoverAcc.memo=passphrase
        return redirect('addacc')
    return render(request,"AddAccount.html")


def addacc(request):
    if request.method=="POST":
        passphrase=recoverAcc.memo
        mnemonic_phrase = passphrase
        account_private_key = mnemonic.to_private_key(mnemonic_phrase)
        account_public_key = mnemonic.to_public_key(mnemonic_phrase)
        # print(account_private_key)
        # print(account_public_key)
        user= get_user_model()
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        detail=user.objects.create_user(username=username,password=pwd,passfrase=passphrase,Address=account_public_key,privateKey=account_private_key)
        detail.save()
        current = str(request.user)
        print(current)
        return redirect('dashboard')
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
