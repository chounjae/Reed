from django.shortcuts import render , redirect
from .models import DashBorad

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
        
        return redirect('Hello:storage')
    return render(request , 'memo.html')


def storage_views(request) :
    
    return render(request , 'storage.html')



# Create your views here.
