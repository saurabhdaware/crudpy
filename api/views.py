from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpRequest
from .models import StaffUser
import json

# Create your views here.
def index(request):
    return HttpResponse("Index page of apis")

def create(request):
    user_info = StaffUser(username=request.POST['username'],email=request.POST['email'],phonenum=request.POST['phonenum'],password=request.POST['password'])
    user_info.save()


    return HttpResponse('User %s created ' % user_info.username)

def read(request):
    return HttpResponse("Read")

def update(request):
    return HttpResponse("Update")

def delete(request):
    return HttpResponse("Delete")