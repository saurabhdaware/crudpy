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

    response = {}
    response['username'] = user_info.username
    response['email'] = user_info.email
    json_data = json.dumps(response)
    return HttpResponse(json_data)

def read(request):
    user_info = StaffUser.objects.all()
    json_data = serializers.serialize('json', user_info)
    return HttpResponse(json_data)

def update(request,user_email):
    data = {}
    if(request.method == 'POST'):
        user_info = StaffUser.objects.get(email=user_email)
        if('password' in request.POST):
            user_info.password = request.POST['password']
        if('phonenum' in request.POST):
            user_info.phonenum = request.POST['phonenum']
        if('username' in request.POST):
            user_info.username = request.POST['username']
        user_info.save()
        data['success'] = 'Data of %s edited successfully' % user_email
        return HttpResponse(json.dumps(data))
    else:
        data['error']='Couldnt read the data on this route'
        return HttpResponse(json.dumps(data))

def delete(request):
    return HttpResponse("Delete")