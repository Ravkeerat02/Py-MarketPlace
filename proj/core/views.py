from django.shortcuts import render , redirect
from item.models import Item, Category
from .forms import SignupForm

# home page
def index(request):
    # adding db
    items= Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request , 'core/index.html',{'categories':categories,'items':items})

# contact page
def contact(request):
    return render(request , 'core/contact.html')

# signup page
def signup(request):
    # check if the request is post
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    form = SignupForm()
    
    return render(request , 'core/signup.html',{
        'form': form
    })