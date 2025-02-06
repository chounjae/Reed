from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import PostDash, Comment, User
from django.core.paginator import Paginator
# Create your views here.
from django.db.models import Q

def index(request) :
    postdash = PostDash.objects.all().order_by('-like_users')
    pages = Paginator(postdash,5)
    search = request.GET.get('search','')
    if search:
        search_list = postdash.filter(
      Q(title__icontains = search) 
    )
        pages = Paginator(search_list,5)
                
        
    page_number = request.GET.get("page")
    page_obj = pages.get_page(page_number)
    context = {"Dashboard": page_obj}
    return render(request,'CUJO/index.html', context)

def dashboard(request, dashboard_id):
    postdash = PostDash.objects.get(pk=dashboard_id)
    context = {"Dashboard": postdash}
    if request.method == "POST":
        reaction = request.POST.get('reaction')
        user = request.user
        if reaction == "like":
            postdash.like += 1  # 좋아요 증가
            postdash.save()  # 변경 사항 저장
            return redirect("CUJO:dashboard",dashboard_id)
        elif reaction == "unlike":
            postdash.unlike += 1  # 싫어요 증가
            postdash.save()  # 변경 사항 저장
            return redirect("CUJO:dashboard",dashboard_id)
        else :
            mains = request.POST["mains"]
            comment = Comment.objects.create(dash=postdash,user=user,mains=mains)
            comment.save()
            return redirect("CUJO:dashboard",dashboard_id)
            


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

def like_view(request, dashboard_id) :
    if request.user.is_authenticated:
        article = PostDash.objects.get(pk=dashboard_id)
        if article.like_users.filter(pk=request.user.pk).exists():
            # 좋아요 취소 (remove)
            article.like_users.remove(request.user)
        else:
            # 좋아요 추가 (add)
            article.like_users.add(request.user)
        return redirect("CUJO:dashboard",dashboard_id)
    return redirect('CUJO:login')

def dislike_view(request, dashboard_id) :
    if request.user.is_authenticated:
        article = PostDash.objects.get(pk=dashboard_id)
        if article.dislike_users.filter(pk=request.user.pk).exists():
            article.dislike_users.remove(request.user)
        else:
            article.dislike_users.add(request.user)
        return redirect("CUJO:dashboard",dashboard_id)
    return redirect('CUJO:login')