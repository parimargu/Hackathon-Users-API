from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.response import HttpResponse


# Create your views here.

def welcome_note(request):
    content = {"message": "User Management API"}
    return JsonResponse(data=content)


def hello(request):
    return HttpResponse("Hello World!")


def create_user(request):
    content = {}
    return JsonResponse(data=content)


def get_user(request):
    content = {}
    return  JsonResponse(data=content)


def list_users(request):
    content = []
    return JsonResponse(data=content)
