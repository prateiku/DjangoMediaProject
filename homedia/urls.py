from django.urls import path
from . import views

urlpatterns = [
    path('',views.media, name='media'),
    path('<str:video>',views.media_handling, name='media_handling'),
]