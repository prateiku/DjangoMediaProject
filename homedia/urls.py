from django.urls import path
from . import views

urlpatterns = [
    path('',views.mediaUser, name='media_user'),
    path('<str:video>',views.media_handling, name='media_handling'),
]