from django.shortcuts import render , redirect
from .models import DashBoard
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout , login

@login_required
def index_views(request):
    
    return render(request , 'index.html')

#메모 작성 page , memo.html
@login_required
def memo_views(request):
    if request.method == 'POST':
        title = request.POST['title']
        main_text = request.POST['main_text']
        
        #db에 저장
        content = DashBoard.objects.create(title = title , main_text = main_text)
        content.save()
        
        #DB 데이터 html에 연결
        return redirect('Hello:storage') 
    return render(request , 'memo.html')

#작성 된 메모 리스트 페이지
@login_required
def storage_views(request) :
    postdash = DashBoard.objects.all()
    pages = Paginator(postdash, 5)
    page_number = request.GET.get("page")
    page_obj = pages.get_page(page_number)
    context = {"dashboard": page_obj}
    return render(request , 'storage.html' , context)

#메모 상세 내용 페이지
@login_required
def storage_IDviews(request , storage_id) :
    #pk 값이 일치하면 db data를 가져옴
    IDviews = DashBoard.objects.get(pk = storage_id)
    IDviews.save()
    
    return render(request , 'memo_detail.html' , {'dashborad': IDviews})

@login_required
def logout_views(request) :
    logout(request)
    return redirect('Users:first_page')




# Create your views here.
