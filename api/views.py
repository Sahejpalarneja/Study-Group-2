

import api
from .serializer import MessageSerilizer, SubjectSerializer,SubjectStudentSerializer, UserSerializer
from main.models import Message,Subject
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


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
def get_messages(request,neptun):
    messages = Message.objects.filter(N_code = neptun).order_by('timestamp')
    serializer = MessageSerilizer(messages, many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET',])
@permission_classes([])
def get_subjects(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects,many = True)
    return JsonResponse(serializer.data, safe = False)
