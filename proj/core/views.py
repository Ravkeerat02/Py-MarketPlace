from django.shortcuts import render

# Create your views here.
# info about browser - request
# home page
def index(request):
    return render(request , 'core/index.html')
# contact page
def contact(request):
    return render(request , 'core/contact.html')