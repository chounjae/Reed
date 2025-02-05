from django.shortcuts import render , redirect
from .models import User
from django.contrib.auth import login , logout , authenticate

#첫 로딩 페이지
def first_views(request) :    
    return render(request , 'first_page.html')

#회원 가입 페이지
def signup_views(request) :
    if request.method == 'POST' :       
        UserInfo = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password'],
        )
        UserInfo.save()
        
        return redirect('Users:first_page')
    return render(request , 'signup.html')
    
    
#로그인 페이지
#성공 >> index.html 로드
#실패 >> login.html 다시 로드
def login_views(request) :
    if request.method == 'POST' :
        username = request.POST["username"]
        password = request.POST["password"]
        
        UserInfo = authenticate(request , username = username , password = password)
        
        if UserInfo is not None:
            #사용자를 로그인 상태로 만듦
            login(request , UserInfo)
            return redirect('Hello:index')
        else:
            print(f"로그인 실패 : {UserInfo}")
        
    return render(request , 'login.html')


    

# Create your views here.
