from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    # path('',views.homepage, name='homepage'),
    path('media-login',views.mediaLogin, name='media_login'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
]