from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request) :
    return render(request,'CUJO/index.html')

def dashboard(request) :
    return render(request,'CUJO/content.html')

def login_view(request) :
    if request.method == 'POST' :
        print(request.POST)
    return render(request,'CUJO/login.html')