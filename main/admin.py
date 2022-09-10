from django.contrib import admin
from .models import Subject,SubjectStudent,Message

admin.site.register(Subject)
# Register your models here.
admin.site.register(SubjectStudent)
admin.site.register(Message)