from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpRequest
from .models import StaffUser
import json

# Create your views here.
def index(request):
    return HttpResponse("Index page of apis")

def create(request):
    return HttpResponse(json.dumps(request.POST))

def read(request):
    return HttpResponse("Read")

def update(request):
    return HttpResponse("Update")

def delete(request):
    return HttpResponse("Delete")