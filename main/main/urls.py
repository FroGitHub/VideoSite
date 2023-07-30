from django.contrib import admin
from django.urls import path, include
from main import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('videosite.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)