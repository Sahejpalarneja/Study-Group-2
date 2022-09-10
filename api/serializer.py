from rest_framework import serializers
from ..main.models import Subject,SubjectStudent,Message 

class SubjectSerializer(serializers.ModelSerializer):
    