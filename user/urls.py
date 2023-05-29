from django.urls import path
from .views import register, user_list

urlpatterns = [
    path('register/', register, name='register'),
    path('users/', user_list, name='user_list'),
]
