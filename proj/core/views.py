from django.shortcuts import render
from item.models import Item, Category

# home page
def index(request):
    # adding db
    items= Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request , 'core/index.html',{'categories':categories,'items':items})

# contact page
def contact(request):
    return render(request , 'core/contact.html')