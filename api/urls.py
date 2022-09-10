from django.urls import path,include
from api import views
app_name = 'api'
urlpatterns = [
    path('messages/<str:neptun>',views.get_messages,name = 'messages'),
    path('subjects',views.get_subjects,name = 'subjects'),
    path('register',views.regiter_user,name = 'register'),
]