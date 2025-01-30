from django.shortcuts import render

def index_views(request):
    return render(request , 'index.html')

def memo_views(request):
    return render(request , 'memo.html')


# Create your views here.
