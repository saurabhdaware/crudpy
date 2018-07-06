from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpRequest,JsonResponse
from .models import StaffUser
import json
from django.core import serializers

# Create your views here.
def index(request):
    return HttpResponse("Index page of apis")

def validate(request):
    username = request.POST['username']
    email = request.POST['email']
    phonenum = request.POST['phonenum']
    password = request.POST['password'] # Hash password here
    if(username.strip() == '' or len(username)>20):
        return False
    else:
        return True


def create(request):
    response = {}
    if(request.method == 'POST' and validate(request)):
        user_info = StaffUser(username=request.POST['username'],email=request.POST['email'],phonenum=request.POST['phonenum'],password=request.POST['password'])
        user_info.save()
        response['username'] = user_info.username
        response['email'] = user_info.email
        return JsonResponse(response)
    else:
        response['error'] = 'Couldnt read the data of user or validation failed'
        return JsonResponse(response)


def read(request):
    user_info = StaffUser.objects.all()
    json_data = serializers.serialize('json', user_info)
    return HttpResponse(json_data)

def update(request,user_username):
    data = {}
    if(request.method == 'POST'):
        user_info = StaffUser.objects.get(username=user_username)
        if('password' in request.POST):
            user_info.password = request.POST['password']
        if('phonenum' in request.POST):
            user_info.phonenum = request.POST['phonenum']
        if('email' in request.POST):
            user_info.email = request.POST['email']
        user_info.save()
        data['success'] = 'Data of %s edited successfully' % user_username
        return JsonResponse(data)
    else:
        data['error']='Couldnt read the data on this route'
        return JsonResponse(data)

def delete(request,user_username):
    response = {}
    try:
        user_info = StaffUser.objects.get(username=user_username)
        user_info.delete()
        response['success'] = '%s succesfully deleted from database'%user_username
        return JsonResponse(response)
    except:
        response['error'] = '%s User not present in database'%user_username
        return JsonResponse(response)
    