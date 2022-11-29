
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from .forms import SubjectModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
import json
from django.http import HttpResponseRedirect


from django.views import View
from .models import Subject, SubjectStudent,Message
# Create your views here.
class MainPageView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        student = request.user
        subject_ids = SubjectStudent.objects.filter(student_id = student.id).only('subject_id')
        subjects = [Subject.objects.get(neptun = id)for id in subject_ids]
        ctx = {'user':student,'subjects':subjects}
        return render(request,'main/main.html',ctx)

class SubjectCreate(LoginRequiredMixin,BSModalCreateView):
    template_name = 'main/subject_form.html'
    form_class = SubjectModelForm
    success_message = 'Success: Subject was added'
    success_url = reverse_lazy('main:main')

    def form_valid(self,form):
        if self.request.is_ajax():
            obj = form.save(commit=False)
            try:
                old = Subject.objects.get(neptun = obj.neptun)
                print(old.name)
                return HttpResponseRedirect(self.success_url)
            except:
                student_id = self.request.user.id
                subject_id = obj.neptun
                subject_student = SubjectStudent(student_id = student_id,subject_id = subject_id)
                print(subject_student.subject_id)
                obj.save()
                subject_student.save()
                return HttpResponseRedirect(self.success_url)
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
        sender = request.POST['sender']
        message = request.POST['message']
        timestamp = datetime.now()
        subject = request.POST['subject']
        n_code = Subject.objects.get(name = subject)
        message_obj = Message(sender = sender,text = message.strip(),N_code = n_code.neptun ,timestamp = timestamp)
        message_obj.save()
        return HttpResponse('Success')
    return HttpResponse("Dikkat")

def get_message(request):
    if request.method == 'GET':
        subject = Subject.objects.get(name = request.GET['subject'] )
        l = Message.objects.filter(N_code = subject.neptun).order_by('timestamp')
        print(len(l))
        message_list = [{'sender':message.sender,'text':message.text,'datetime':''.join(str(message.timestamp).split('.')[:-1])} for message in l ]
        message_list = json.dumps(message_list,indent=2)
        return HttpResponse(message_list)
        
