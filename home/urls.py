from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_page_view,name='homepage'),
    path('/register',views.register_page,name='register'),
    path('/login',views.login_page,name = 'login')
]