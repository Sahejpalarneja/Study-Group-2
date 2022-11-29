import datetime
from email import message
from .serializer import MessageSerilizer, SubjectSerializer, UserSerializer
from main.models import Message,Subject,SubjectStudent
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from api import serializer


@api_view(['GET',])
@permission_classes([])
def get_subjects(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects,many = True)
    return JsonResponse(serializer.data, safe = False)

# Create your views here.
@api_view(['POST',])
@permission_classes([])
def regiter_user(request):
    serializer =UserSerializer(data = request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        token  =Token.objects.get(user = user).key
        data['username'] = user.username
        data['id'] = user.id
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)


@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def get_messages(request):
    neptun = request.GET['neptun']
    messages = Message.objects.filter(N_code = neptun).order_by('timestamp')
    serializer = MessageSerilizer(messages, many = True)
    return JsonResponse(serializer.data,safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_id(request):
    data = {}
    try:
        id = User.objects.get(username = request.GET['username']).pk    
        data['id'] = id 
    except:
        data['id'] = 'This is id'
    return Response(data)

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def get_user_classes(request):
    user_id = request.GET['id']
    subject_ids = SubjectStudent.objects.filter(student_id = user_id).only('subject_id')
    subjects = [Subject.objects.get(neptun = id)for id in subject_ids]
    serializer = SubjectSerializer(subjects,many = True)
    return JsonResponse(serializer.data, safe = False)

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def join_class(request):
    neptun = request.GET['neptun']
    user_id = request.GET['id']
    subject_student = SubjectStudent(student_id = user_id , subject_id = neptun)
    subject_student.save()
    return Response('Class Joined')


@api_view(['POST',])
@permission_classes([IsAuthenticated])
def add_subject(request):
    serializer = SubjectSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Subject Added')
    else:
        return Response('Data not valid')

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def send_message(request):
    data = request.data
    data._mutable = True
    data['timestamp'] = datetime.datetime.now()
    data._mutable = False
    serializer = MessageSerilizer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response('Sent')
    else:
        return Response('Wrong values')
