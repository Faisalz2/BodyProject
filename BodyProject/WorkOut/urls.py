from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.wlcpag, name = 'wlc'),
path('d',views.calculate_calories_view,name='User'),
path('login/', views.user_login, name='login'),
path('signup/', views.user_signup, name='signup'),
path('logout/', views.user_logout, name='logout'),
path('pl/', views.Create, name='pl'),
]
