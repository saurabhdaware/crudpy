from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpRequest,JsonResponse
from .models import StaffUser
import json
from django.core import serializers

# Create your views here.
def index(request):
    return HttpResponse("Index page of apis")

def create(request):
    user_info = StaffUser(username=request.POST['username'],email=request.POST['email'],phonenum=request.POST['phonenum'],password=request.POST['password'])
    user_info.save()

    return HttpResponse('User %s created ' % user_info.username)
    values = []

def read(request):
    user_info = StaffUser.objects.all()
    json_data = serializers.serialize('json', user_info)
    return HttpResponse(json_data)

def update(request):
    return HttpResponse("Update")

def delete(request):
    return HttpResponse("Delete")