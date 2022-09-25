
from rest_framework import serializers
from  main.models import Subject,SubjectStudent,Message 
from django.contrib.auth.models import User

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name','neptun','professor']

class SubjectStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectStudent
        fields = ['student_id','subject_id']

class MessageSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender','text','N_code','timestamp']

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ["username", "email", "password","password2"]
        extra_kwarg = {
            'password':{'write_only':True},
            
        }
    def save(self):
        user  = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password1 != password2:
            raise serializers.ValidationError({'password':'Passwords must match'})
        user.set_password(password1)
        user.save()
        return user