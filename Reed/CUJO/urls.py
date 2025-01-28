from django.contrib import admin
from django.urls import path
from . import views

app_name = 'CUJO'

urlpatterns = [
    path("login/", views.login_view, name='login'),
    path('', views.index,name='index'),
    path('<int:dashboard_id>/', views.dashboard, name='dashboard')
]