from django.contrib import admin
from django.urls import path
from . import views

app_name = 'CUJO'

urlpatterns = [
    path("login/", views.login_view, name='login'),
    path('', views.index,name='index'),
    path('<int:dashboard_id>/', views.dashboard, name='dashboard'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.signup_view, name='signup'),
    path('write/',views.write_dash, name='write'),
    path('<int:dashboard_id>/like/',views.like_view,name='likes'),
    path('<int:dashboard_id>/dislike/',views.dislike_view,name='dislikes')
]