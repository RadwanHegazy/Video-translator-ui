from django.contrib import admin
from django.urls import path, re_path
from app.views import download, home
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('download',download,name='download'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)