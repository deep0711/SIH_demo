from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def home(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request,'CHATapp/index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        context={}
        form = Registerform()
        if request.method=="POST":
            form = Registerform(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Your account created successfully!!')
                return redirect('loginpage')
        
        context['form']=form
        return render(request,'CHATapp/register.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user = authenticate(request,username=username,password=password)
            
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in Successfully as '+ username)
                return redirect('index')
            else:
                messages.info(request,'Username or Password is wrong!')
                return render(request,'CHATapp/login.html')
                    
        return render(request,'CHATapp/login.html')

@login_required(login_url='loginpage')
def index(request):
    return render(request,'CHATapp/home.html')

@login_required(login_url='loginpage')
def logoutuser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='loginpage')
def alert(request):
    return render(request,'CHATapp/alert.html')

@login_required(login_url='loginpage')
def tab(request):
    return render(request,'CHATapp/table-basic.html')
