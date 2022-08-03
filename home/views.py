
from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request,'home.html')

def login_page(request):
    return render(request,'registration/login.html')

def register_page(request):
    return render(request,'registration/register.html')