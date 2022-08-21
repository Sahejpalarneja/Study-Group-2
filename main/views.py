
from django.shortcuts import render
from .forms import SubjectModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from django.http import HttpResponseRedirect


from django.views import View
from .models import Subject, SubjectStudent
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
    success_url = reverse_lazy('main:main')

    def form_valid(self,form):
        if not self.request.is_ajax():
            obj = form.save(commit=False)
            student_id = self.request.user.id
            subject_id = obj.neptun
            subject_student = SubjectStudent(student_id = student_id,subject_id = subject_id)
            obj.save()
            subject_student.save()
        return HttpResponseRedirect(self.success_url)
    
def join_class(request):
    subjects = Subject.objects.all()
    ctx = {'subjects':subjects}
    return render(request,'main/join-class.html',ctx)