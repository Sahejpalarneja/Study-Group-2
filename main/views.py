from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.
class MainPageView(LoginRequiredMixin,View):
    def get(self,request):
        ctx = {'user':request.user}
        return render(request,'main/main.html',ctx)