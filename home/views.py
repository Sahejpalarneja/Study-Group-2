from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token
# Create your views here.

def home_page(request):
	return render(request,'home.html')

def login_page(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("main:main")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})

def register_page(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("main:main")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})


@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance = None,created= False, **kwargs):
	if created:
		Token.objects.create(user = instance)

def logout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")