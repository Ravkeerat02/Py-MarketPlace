from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    #    home
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    # delete
    path('<int:pk>/delete/', views.delete, name='delete'),
    # update
    path('<int:pk>/edit', views.edit, name='edit'),
    # # list
    # path('', views.list, name='list'),
    
 
]
