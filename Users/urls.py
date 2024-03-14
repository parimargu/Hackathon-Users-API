from django.urls import path
from .views import welcome_note, hello, create_user, get_user, list_users

urlpatterns = [
    path('', welcome_note, name="welcome_note"),
    path('hello', hello, name="hello"),
    path('create_user/', create_user, name="create_user"),
    path('get_user/', get_user, name="get_user"),
    path('list_users/', list_users, name='list_users'),
]