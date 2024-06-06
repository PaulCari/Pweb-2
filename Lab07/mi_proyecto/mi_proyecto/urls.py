from django.contrib import admin
from django.urls import path, include
from destinos.views import listar_destinos
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_destinos, name='home'),
    path('destinos/', include('destinos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



