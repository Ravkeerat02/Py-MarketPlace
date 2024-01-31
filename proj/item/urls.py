from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
   
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    # delete
    path('<int:pk>/delete/', views.delete, name='delete'),
    # update
    path('<int:pk>/edit', views.edit, name='edit'),
    # # list
    # path('', views.list, name='list'),
    
 
]
