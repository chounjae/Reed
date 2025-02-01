from django.shortcuts import render , redirect
from .models import DashBorad
from django.core.paginator import Paginator

def index_views(request):
    
    return render(request , 'index.html')

#메모 작성 page , memo.html
def memo_views(request):
    if request.method == 'POST':
        title = request.POST['title']
        main_text = request.POST['main_text']
        
        #db에 저장
        content = DashBorad.objects.create(title = title , main_text = main_text)
        content.save()
        
        #DB 데이터 html에 연결
        return redirect('Hello:storage') 
    return render(request , 'memo.html')

#작성 된 메모 리스트 페이지
def storage_views(request) :
    postdash = DashBorad.objects.all()
    pages = Paginator(postdash, 5)
    page_number = request.GET.get("page")
    page_obj = pages.get_page(page_number)
    context = {"dashboard": page_obj}
    return render(request , 'storage.html' , context)

#메모 상세 내용 페이지
def storage_IDviews(request , storage_id) :
    #pk 값이 일치하면 db data를 가져옴
    IDviews = DashBorad.objects.get(pk = storage_id)
    IDviews.save()
    
    return render(request , 'Hello/memo_detail.html' , {'dashborad': IDviews})



# Create your views here.
