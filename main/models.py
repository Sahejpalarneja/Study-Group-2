from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
# Create your models here.
class Subject(models.Model):
    class Meta:
        app_label = 'main'

    name = models.CharField(
        max_length=200,
        help_text='Enter the name of the Group/Forum',
        validators=[MinLengthValidator(1,"Please enter a Group/forum name")]
    )
    neptun =  models.CharField(
        max_length=10,
        help_text='Enter the subject/forum code',
        validators=[MinLengthValidator(1,"Please Enter a group/forum code")]
    )
    professor = models.CharField(
        max_length=200,
        help_text="Enter the name of the admin if exists"
    )

    def __str__(self) -> str:
        return self.name

class SubjectStudent(models.Model):
    class Meta:
        app_label = 'main'
    student_id = models.IntegerField()
    subject_id = models.CharField(max_length= 10,validators=[MinLengthValidator(1)])

    def __str__(self) -> str:
        return self.subject_id
    

class Message(models.Model):
    class Meta:
        app_label = 'main'
    sender = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    text = models.TextField()
    N_code = models.CharField(max_length = 10,validators=[MinLengthValidator(1,"Please Enter a subject/forum code")])
    timestamp = models.DateTimeField()

    def __str__(self):
        subject = Subject.objects.get(neptun = self.N_code)
        return subject.name +'_'+ self.sender