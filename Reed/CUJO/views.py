from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import PostDash, Comment, User, Author
# Create your views here.


def index(request) :
    postdash = PostDash.objects.order_by('-like')[:10]
    context = {"Dashboard": postdash}
    return render(request,'CUJO/index.html', context)

def dashboard(request, dashboard_id):
    postdash = PostDash.objects.get(pk=dashboard_id)
    context = {"Dashboard": postdash}
    if request.method == "POST":
        reaction = request.POST.get('reaction')
        if reaction == "like":
            postdash.like += 1  # 좋아요 증가
        elif reaction == "unlike":
            postdash.unlike += 1  # 싫어요 증가
        postdash.save()  # 변경 사항 저장
        

    return render(request,'CUJO/content.html',context)

def login_view(request) :
    if request.method == 'POST' :
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password = password)
        if user is not None :
            print('성공')
            login(request, user)
        else :
            print('실패')
    return render(request,'CUJO/login.html') 

def logout_view(request) :
    logout(request)
    return redirect("CUJO:index")

def signup_view(request) :
    if request.method == 'POST' :
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('CUJO:index')
    return render(request,'CUJO/signup.html')

def write_dash(request) :
    if request.method == 'POST' :
        title = request.POST["title"]
        main = request.POST["main"]
        user = request.user
        #author = Author.objects.get(id=1)
        dash = PostDash.objects.create(title=title,user=user,main=main)
        dash.save()
        return redirect('CUJO:index')
    return render(request,'CUJO/write.html')