from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'api'
urlpatterns = [
    path('get_messages',views.get_messages,name = 'get_messages'),
    path('subjects',views.get_subjects,name = 'subjects'),
    path('register',views.regiter_user,name = 'register'),
    path('login',obtain_auth_token,name = 'login'),
    path('get_id',views.get_user_id,name='get_id'),
    path('get_user_subjects',views.get_user_classes,name='user_classes'),
    path('join_class',views.join_class,name='join_class'),
    path('add_subject',views.add_subject,name='add_subject'),
    path('send_message',views.send_message,name='send_message')
]