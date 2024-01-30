from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    # Other paths...
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    # Other paths...
]
