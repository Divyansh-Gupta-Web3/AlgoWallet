from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

def index(request):
    user= get_user_model()
    if request.method=="POST":
        username = request.POST.get('username')
        pas = request.POST.get('password')
        passfrase = request.POST.get('passfrase')
        address = request.POST.get('address')
        privatekey = request.POST.get('username')

        detail=user.objects.create_user(username=username,password=pas,passfrase=passfrase,Address=address,privateKey=privatekey)
        detail.save()

        current = str(request.user)
        print(current)

    return render(request,'test.html')
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
    params={"name":"Divyansh"}
    return render(request,"dashboard.html",params)