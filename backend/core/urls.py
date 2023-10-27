from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from ckeditor_uploader import views as ckeditor_uploader_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.api.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)