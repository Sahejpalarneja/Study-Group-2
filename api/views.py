from django.shortcuts import render
from .serializer import MessageSerilizer, SubjectSerializer,SubjectStudentSerializer, UserSerializer
from main.models import Message,Subject
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api import serializer

# Create your views here.
@api_view(['POST',])
def regiter_user(request):
    serializer =UserSerializer(data = request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'registered'
    else:
        data = serializer.errors
    return Response(data)


def get_messages(request,neptun):
    messages = Message.objects.filter(N_code = neptun).order_by('timestamp')
    serializer = MessageSerilizer(messages, many = True)
    return JsonResponse(serializer.data,safe=False)

def get_subjects(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects,many = True)
    return JsonResponse(serializer.data, safe = False)
