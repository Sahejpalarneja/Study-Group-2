from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
# Create your models here.
class Subject(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Enter the name of the Subject/Forum',
        validators=[MinLengthValidator(1,"Please enter a subject/forum name")]
    )
    neptun =  models.CharField(
        max_length=10,
        help_text='Enter the subject/forum code',
        validators=[MinLengthValidator(1,"Please Enter a subject/forum code")]
    )
    professor = models.CharField(
        max_length=200,
        help_text="Enter the name of the Professor if exists"
    )

    def __str__(self) -> str:
        return self.name

class SubjectStudent(models.Model):
    student_id = models.IntegerField()
    subject_id = models.CharField(max_length= 10,validators=[MinLengthValidator(1)])

    def __str__(self) -> str:
        return self.subject_id