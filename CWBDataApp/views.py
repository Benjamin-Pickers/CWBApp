from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Batchcosttracking

def index(request):
    return render(request, 'CWBDataApp/index.html')

def BatchCostTracking(request):
    return HttpResponse('Hello world')

def MaterialTesting(request):
    return HttpResponse('')
