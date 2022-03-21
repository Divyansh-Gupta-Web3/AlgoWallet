from pprint import pprint
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
from algosdk.v2client import indexer
from algosdk import mnemonic

passphrase=[]

# def index(request):

#     # algod_token = '4xcfeVtFO21zGa5oJr3us3bpzXACJjQg5oPUdTtv'
#     # algod_address = 'https://testnet-algorand.api.purestake.io/idx2'
#     # purestake_token = {'X-API-Key': algod_token}
#     # acl = indexer.IndexerClient(algod_token, algod_address,headers=purestake_token)
#     # response = acl.search_transactions(address="JHIBASZEKIAANRRBNU4UTDJ2NLI4ZYRW6UHKHWTTMFUDK7CESTVYC3TEQI")
#     # owner="JHIBASZEKIAANRRBNU4UTDJ2NLI4ZYRW6UHKHWTTMFUDK7CESTVYC3TEQI"
#     # amt=(response["transactions"])
#     # kampy=[]
#     # sno=0
#     # for amt in amt:
#     #   id=amt["id"]
#     #   cnfround=amt["confirmed-round"]
#     #   amount=amt["payment-transaction"]["amount"]
#     #   sender=amt["sender"]
#     #   receiver=amt["payment-transaction"]["receiver"]
#     #   fee=amt["fee"]
#     #   if sender==owner:
#     #       tnxtype="Sent"
#     #   else:
#     #       tnxtype="Receive"
#     #   sno=sno+1
#     #   divyansh= {"sno":sno,"id":id,"cnfround":cnfround,"amount":amount,"receiver":receiver,"sender":sender ,"fee":fee,"tnxtype":tnxtype}
#     #   kampy.append(divyansh)
#     #   sno
#     # user= get_user_model()
#     # if request.method=="POST":
#     #     username = request.POST.get('username')
#     #     pas = request.POST.get('password')
#     #     passfrase = request.POST.get('passfrase')
#     #     address = request.POST.get('address')
#     #     privatekey = request.POST.get('privatekey')

#     #     detail=user.objects.create_user(username=username,password=pas,passfrase=passfrase,Address=address,privateKey=privatekey)
#     #     detail.save()

#     #     current = str(request.user)
#     #     print(current)

#     return render(request,'index.html',{'magic':'','name':'Divyansh','bal':'245'})  
#       #,{'divyansh':kampy})
# # Create your views here.
# def signin(request):
#     if request.method == "POST":
#         name = request.POST.get('username')
#         pwd = request.POST.get('password')          
#         user = authenticate(request, username=name,password=pwd)
#         if user is not None:
#             login(request,user)
#             current = str(request.user.username)
#             print(current)
#             return redirect("dashboard")
#         else:
#             return redirect("login")          
#     return render(request,"login.html")

# @login_required(login_url="/signin/")
# def dashboard(request): 
   
#     return render(request,"dashboard.html") 

def AddAccount(request):
    holders={
        "Words1":
        {
        "word1":"Word1",
        "word2":"Word2",
        "word3":"Word3",
        "word4":"Word4",
        "word5":"Word5",
        },
         "Words2":
        {
        "word6":"Word6",
        "word7":"Word7",
        "word8":"Word8",
        "word9":"Word9",
        "word10":"Word10",
        },
         "Words3":
        {
        "word11":"Word11",
        "word12":"Word12",
        "word13":"Word13",
        "word14":"Word14",
        "word15":"Word15",
        },
         "Words4":
        {
        "word16":"Word16",
        "word17":"Word17",
        "word18":"Word18",
        "word19":"Word19",
        "word20":"Word20",
        },
         "Words5":
        {
        "word21":"Word21",
        "word22":"Word22",
        "word23":"Word23",
        "word24":"Word24",
        "word25":"Word25",
        },
    } 
    if request.method=="POST":
        p1 = request.POST.get('word1')
        p2 = request.POST.get('word2')
        p3 = request.POST.get('word3')
        p4 = request.POST.get('word4')
        p5 = request.POST.get('word5')
        p6 = request.POST.get('word6')
        p7 = request.POST.get('word7')
        p8 = request.POST.get('word8')
        p9 = request.POST.get('word9')
        p10 = request.POST.get('word10')
        p11 = request.POST.get('word11')
        p12 = request.POST.get('word12')
        p13 = request.POST.get('word13')
        p14 = request.POST.get('word14')
        p15 = request.POST.get('word15')
        p16 = request.POST.get('word16')
        p17 = request.POST.get('word17')
        p18 = request.POST.get('word18')
        p19 = request.POST.get('word19')
        p20 = request.POST.get('word20')
        p21 = request.POST.get('word21')
        p22 = request.POST.get('word22')
        p23 = request.POST.get('word23')
        p24 = request.POST.get('word24')
        p25 = request.POST.get('word25')  
        print(p10)
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
        AddAccount.memo=passphrase
        return redirect('createRecovery')
    return render(request,"AddAccount.html",holders)


# def addacc(request):
    #  if request.method=="POST":
    #     passphrase=AddAccount.memo
    #     mnemonic_phrase = passphrase
    #     account_private_key = mnemonic.to_private_key(mnemonic_phrase)
    #     account_public_key = mnemonic.to_public_key(mnemonic_phrase)
    #     # print(account_private_key)
    #     # print(account_public_key)
    #     user= get_user_model()
    #     username = request.POST.get('AccName')
    #     pwd = request.POST.get('AccPwd')
    #     detail=user.objects.create_user(username=username,password=pwd,passfrase=passphrase,Address=account_public_key,privateKey=account_private_key)
    #     detail.save()
    #     current = str(request.user)
    #     print(current)
    #     return redirect('login')
    # return render(request,"AddAccount2.html")

# @login_required(login_url="/login/")
# def history(request):
#     return render(request,"history.html")

# @login_required(login_url="/login/")
# def send(request):
#     return render(request,"send.html")

# @login_required(login_url="/login/")
# def recieve(request):
#     return render(request,"recieve.html")


# def newacc(request):
#     return render(request,"NewAccount.html")

# def base(request):
#     return render(request,"base.html",{'magic':'','name':'name','bal':'245'})



def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == "POST":
        name = request.POST.get('AccName')
        pwd = request.POST.get('AccPwd')          
        user = authenticate(request, username=name,password=pwd)
        if user is not None:
            login(request,user)
            current = str(request.user.username)
            print(current)

            return redirect("dashboard")
        else:
            return redirect("signin")          
    return render(request,"login.html")

 
# def (request):
    

#     return render(request, "AddAccount.html",holders)

def CreateAccount(request):
    return render(request, "CreateAccount.html")

def dashboard(request):
    return render(request, "dashboard.html")

    
def SendAlgo(request):
    return render(request, "send.html")
def RecieveAlgo(request):
    return render(request, "recieve.html")
def History(request):
    return render(request, "history.html")
def createRecovery(request):
    if request.method=="POST":
        passphrase=AddAccount.memo
        mnemonic_phrase = passphrase
        account_private_key = mnemonic.to_private_key(mnemonic_phrase)
        account_public_key = mnemonic.to_public_key(mnemonic_phrase)
        # print(account_private_key)
        # print(account_public_key)
        user= get_user_model()
        username = request.POST.get('AccName')
        pwd = request.POST.get('AccPwd')
        print(username)
        print(pwd)
        detail=user.objects.create_user(username=username,password=pwd,passfrase=passphrase,Address=account_public_key,privateKey=account_private_key)
        detail.save()
        current = str(request.user)
        print(current)
        return redirect('signin')
    return render(request, "createRecovery.html")




