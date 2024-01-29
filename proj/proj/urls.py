
from django.contrib import admin
from django.urls import include, path
from core.views import index , contact
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # home
    path('',index,name='index'),
    # item
    path('items/',include('item.urls')),
    # contact
    path('contact/',contact,name='contact'),
    # main
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
