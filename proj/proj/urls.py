
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # include the main ones
    path('' , include('core.urls')),
    # item
    path('items/',include('item.urls')),
    
    # main
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)