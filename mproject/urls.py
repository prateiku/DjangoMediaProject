"""mproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic.base import TemplateView
from homedia import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/', include('homedia.urls')), #homedia app stream.
    path('auth/', include('django.contrib.auth.urls')), #auth app login/logout/reset.
    path('', include('authentication.urls')),
    path('', views.homepage, name='homepage'),#homedia app
    path('about/',views.about, name='about'), #homedia app about
    path('upload/', views.upload, name='upload'),#homedia app upload
    path('delete/', views.deleted, name='deleted'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

