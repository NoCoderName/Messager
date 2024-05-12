from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

from coolsite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProfileApp.urls')),
    path('', include('ChatApp.urls')),
    path('', include('LoginApp.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)