

from django.contrib import messages
from django.shortcuts import render
from .forms import SubjectModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from django.http import HttpResponseRedirect,response


from django.views import View
from .models import Subject, SubjectStudent,Message
# Create your views here.
class MainPageView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        student = request.user
        subject_ids = SubjectStudent.objects.filter(student_id = student.id).only('subject_id')
        subjects = [Subject.objects.get(neptun = id)for id in subject_ids]
        messages ={}
        for subject in subjects:
            l = Message.objects.filter(N_code = subject.neptun).order_by('-timestamp')
            if l is None:
                messages[subject.name] = None
            else:
                message_list = [{'sender':message.sender,'text':message.text} for message in l ]
                messages[subject.name] = message_list
        ctx = {'user':student,'subjects':subjects,'messages':messages}
        return render(request,'main/main.html',ctx)

class SubjectCreate(LoginRequiredMixin,BSModalCreateView):
    template_name = 'main/subject_form.html'
    form_class = SubjectModelForm
    success_message = 'Success: Subject was added'
    success_url = reverse_lazy('main:main')

    def form_valid(self,form):
        if not self.request.is_ajax():
            obj = form.save(commit=False)
            if Subject.objects.get(neptun = obj.neptun):
                return HttpResponseRedirect(self.success_url)
            student_id = self.request.user.id
            subject_id = obj.neptun
            subject_student = SubjectStudent(student_id = student_id,subject_id = subject_id)
            obj.save()
            subject_student.save()
        return HttpResponseRedirect(self.success_url)
    

class SubjectJoin(LoginRequiredMixin,View):
    template_name = 'main/join-class.html'
    success_url = reverse_lazy('main:main')
    
    def get(self,request):
        subjects = Subject.objects.all()
        ctx = {'subjects':subjects}
        return render(request,self.template_name,ctx)

    def post(self,request):
        subject_name = request.POST.get('join')
        subject = Subject.objects.get(name= subject_name)
        student = self.request.user
        joined = SubjectStudent.objects.filter(student_id = student.id).filter(subject_id = subject.neptun).count()
        if joined > 0:
            messages.info(request,'Already Enrolled')
        else:
            subject_student = SubjectStudent(student_id = student.id , subject_id = subject.neptun)
            subject_student.save()
            messages.success(request,subject.name+' Joined')
        return HttpResponseRedirect(self.success_url)
    

def send_message(request):
    if request.method == 'POST':
        print("This is working")
        return response(status_code = 210)
    return HTTPResponse("Dikkat")