from dataclasses import field
from re import template
from django.shortcuts import render
from .forms import SubjectModelForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView


from django.views import View
from .models import Subject
# Create your views here.
class MainPageView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        ctx = {'user':request.user}
        return render(request,'main/main.html',ctx)


class SubjectCreate(LoginRequiredMixin,BSModalCreateView):
    template_name = 'main/subject_form.html'
    form_class = SubjectModelForm
    success_message = 'Success: Subject was added'
    success_url = reverse_lazy('autos:all')