from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Batchcosttracking

def index(request):
    return render(request, 'CWBDataApp/index.html')

def BatchCostTracking(request):
    return render(request, 'CWBDataApp/BatchCostTracking.html')

def MaterialTesting(request):
    return render(request, 'CWBDataApp/MaterialTesting.html')

def ProductInventory(request):
    return render(request, 'CWBDataApp/ProductInventory.html')

def MaterialInventory(request):
    return render(request, 'CWBDataApp/MaterialInventory.html')

def OrderSheets(request):
    return render(request, 'CWBDataApp/OrderSheets.html')

def help(request):
    return render(request, 'CWBDataApp/help.html')
