from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from item.models import Item

# main- home
@login_required
def index(request):
    items = Item.objects.filter(created_by = request.user)
    
    return render(request , 'dashboard/index.html', {'items': items})
