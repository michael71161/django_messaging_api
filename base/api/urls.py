from django.contrib import admin
from django.urls import path,include
from . import views 
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    
    path('test/', views.index),
    path('testget/', views.test_getall),
    path('register/', views.register),
    path('logout/',views.myLogout),
    path('signintoken/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('write/', views.writeMsg),
    path('getmsgstouser/', views.getAllUserMsg ),
    path('readmessage/<pk>/', views.markMsgAsRead),
    path('getunrduser/', views.getAllUnrdMsg ),
    path('delmsguser/<pk>/', views.delMsgUser),
    path('',views.get_users),



]
