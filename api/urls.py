from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'api'
urlpatterns = [
    path('messages/<str:neptun>',views.get_messages,name = 'messages'),
    path('subjects',views.get_subjects,name = 'subjects'),
    path('register',views.regiter_user,name = 'register'),
    path('login',obtain_auth_token,name = 'login'),
    path('get_id',views.get_user_id,name='get_id'),
    path('get_user_subjects',views.get_user_classes,name='user_classes')
]