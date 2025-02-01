"""
URL configuration for Reed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'Hello'

urlpatterns = [
   path('' , views.index_views , name = 'index'),
   path('memo/' , views.memo_views , name = 'memo'),
   path('storage/' , views.storage_views , name = 'storage'),
   #int:stor_id 해결 -> 어떻게 int 형식으로 링크 띄울껀지. 
   #그리고 이걸 이용해 어떻게 html에서 for문으로 글 리스트 출력할껀지
   path('storage/<int:storage_id>' , views.storage_IDviews , name = 'storage_IDviews'),
]