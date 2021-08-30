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

