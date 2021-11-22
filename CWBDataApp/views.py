from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Batchcosttracking

def index(request):
    return render(request, 'CWBDataApp/index.html')

def BatchCostTracking(request):


    return render(request, 'CWBDataApp/BatchCostTracking.html')

def BatchCostQuery(request):
    return render(request, 'CWBDataApp/BatchCostQuery.html')

def MaterialTesting(request):
    return render(request, 'CWBDataApp/MaterialTesting.html')

def ProductInventory(request):
    return render(request, 'CWBDataApp/ProductInventory.html')

def MaterialInventory(request):
    return render(request, 'CWBDataApp/MaterialInventory.html')

def OrderSheetsMachine1(request):
    return render(request, 'CWBDataApp/OrderSheetsMachine1.html')

def OrderSheetsMachine2(request):
    return render(request, 'CWBDataApp/OrderSheetsMachine2.html')

def OrderSheetsMachine3(request):
    return render(request, 'CWBDataApp/OrderSheetsMachine3.html')

def help(request):
    return render(request, 'CWBDataApp/help.html')
