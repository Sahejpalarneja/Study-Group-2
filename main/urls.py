from django.urls import path,include
from . import views
app_name = 'main'
urlpatterns = [
    #path('',views.MainPageView.as_view(),name='main'),
    path('',views.MainPageView.as_view(),name='main'),
    path('add',views.SubjectCreate.as_view(),name='add'),
    path('join',views.SubjectJoin.as_view(),name='join'),
    path('sendmessage',views.send_message,name ="send"),
    path('getmessage',views.get_message,name = 'get')
]