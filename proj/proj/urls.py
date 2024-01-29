
from django.contrib import admin
from django.urls import path
from core.views import index , contact


urlpatterns = [
    # home
    path('/',index,name='index'),
    # contact
    path('contact/',contact,name='contact'),
    # main
    path('admin/', admin.site.urls),
]
