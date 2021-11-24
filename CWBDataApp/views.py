from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from .models import Batchcosttracking, Materialcost, Materialinventory, Materialtesting, Ordersheetmachine1, Ordersheetmachine2, Ordersheetmachine3, Picandsum, Productinventory, Productprofiles, Colour

def index(request):
    return render(request, 'CWBDataApp/index.html')

def BatchCostTracking(request):
    allColours = Colour.objects.all()

    if request.method == 'POST':

        form = request.POST

        try:
            if Batchcosttracking.objects.get(pk=request.POST['newBatch']):
                return render(request, 'CWBDataApp/BatchCostTracking.html', {'allColours':allColours, 'error_message' : "Batch already exists, please enter a new batch. If you wish to update a batch talk to an admin",})
        except:
            cost = int(form['weight1'])*float(form['value1']) + int(form['weight2'])*float(form['value2']) + int(form['weight3'])*float(form['value3']) + int(form['weight4'])*float(form['value4'])
            cost=round(cost, 2)
            weight = int(form['weight1']) + int(form['weight2']) + int(form['weight3']) + int(form['weight4'])
            price = round(cost/weight, 2)
            sup1_object = Materialcost.objects.get(pk=form['supplier1'])

            if form['supplier2'] == '':
                sup2_object =  Materialcost.objects.get(pk='None')
            else:
                sup2_object =  Materialcost.objects.get(pk=form['supplier2'])

            if form['supplier3'] == '':
                sup3_object =  Materialcost.objects.get(pk='None')
            else:
                sup3_object =  Materialcost.objects.get(pk=form['supplier3'])

            if form['supplier4'] == '':
                sup4_object =  Materialcost.objects.get(pk='None')
            else:
                sup4_object =  Materialcost.objects.get(pk=form['supplier4'])

            batch = Batchcosttracking(batchname=form['newBatch'],
                                    batchdate=form['batchDate'],
                                    totalcost=cost,
                                    totalweight=weight,
                                    priceperpound=price,
                                    supplier1=sup1_object,
                                    weight1=form['weight1'],
                                    value1=form['value1'],
                                    supplier2=sup2_object,
                                    weight2=form['weight2'],
                                    value2=form['value2'],
                                    supplier3=sup3_object,
                                    weight3=form['weight3'],
                                    value3=form['value3'],
                                    supplier4=sup4_object,
                                    weight4=form['weight4'],
                                    value4=form['value4'],
                                    colour=form['colour'],
                                    colourweight=form['colourWeight'],
                                    colourvalue=form['colourPrice'],
                                    foam= 'Foam',
                                    foamweight=form['foamWeight'],
                                    foamvalue=form['foamPrice'],
                                    totalshredweight=form['shredWeight']
                                    )
            batch.save()



    return render(request, 'CWBDataApp/BatchCostTracking.html', {'allColours':allColours})

def BatchCostQuery(request):
    allColours = Colour.objects.all()
    return render(request, 'CWBDataApp/BatchCostQuery.html')

def MaterialTesting(request):
    allProfiles= Productprofiles.objects.all()
    return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles})

def MaterialTestQuery(request):
    return render(request, 'CWBDataApp/MaterialTestQuery.html')


def ProductInventory(request):

    allProfiles= Productprofiles.objects.all()
    allColours = Colour.objects.all()

    if request.method == 'POST':
        form = request.POST
        prod_object =  Productprofiles.objects.get(pk=form['prodName'])
        if Productinventory.objects.filter(productname=prod_object, colour=form['colour']).exists():

            return render(request, 'CWBDataApp/ProductInventory.html', {'allProfiles':allProfiles, 'allColours':allColours, 'error_message' : "Product already exists in database, please enter a new product. If you wish to update a product scroll down",})
        else:
            newProd = Productinventory(productname=prod_object,
                                       colour=form['colour'],
                                       embossed=form['embossed'],
                                       doublesided=form['doubleSide'],
                                       numberofskids=form['numSkids'])
            newProd.save()
            return render(request, 'CWBDataApp/ProductInventory.html', {'allProfiles':allProfiles, 'allColours':allColours, 'dataAcceptedMessage':"Data Successfully Submitted"})
    return render(request, 'CWBDataApp/ProductInventory.html', {'allProfiles':allProfiles, 'allColours':allColours})


def ProductInventoryUpdate(request):
    allProfiles= Productprofiles.objects.all()
    allColours = Colour.objects.all()

    if request.method == 'POST':
        form = request.POST
        prod_object =  Productprofiles.objects.get(pk=form['prodName'])

        if Productinventory.objects.filter(productname=prod_object, colour=form['colour']).exists():
            prod = Productinventory.objects.get(productname=prod_object, colour=form['colour'])
            prod.numberofskids = form['numSkids']
            prod.save()
            return render(request, 'CWBDataApp/ProductInventoryUpdate.html', {'allProfiles':allProfiles, 'allColours':allColours, 'dataAcceptedMessage':"Product Successfully Updated"})
        else:
            return render(request, 'CWBDataApp/ProductInventoryUpdate.html', {'allProfiles':allProfiles, 'allColours':allColours, 'error_message':"This product currently does not exist in inventory. If you wish to enter its data, press the link above"})
    return render(request, 'CWBDataApp/ProductInventoryUpdate.html', {'allProfiles':allProfiles, 'allColours':allColours})

def ProductInventoryQuery(request):

    allProfiles= Productprofiles.objects.all()
    allColours = Colour.objects.all()

    if request.method == 'POST':
        form = request.POST
        prod_object =  Productprofiles.objects.get(pk=form['prodName'])

        if Productinventory.objects.filter(productname=prod_object, colour=form['colour']).exists():
            prod = Productinventory.objects.get(productname=prod_object, colour=form['colour'])
            prod.numberofskids = form['numSkids']
            prod.save()
            return render(request, 'CWBDataApp/ProductInventoryQuery.html', {'allProfiles':allProfiles, 'allColours':allColours, 'dataAcceptedMessage':"Product Successfully Updated"})

    return render(request, 'CWBDataApp/ProductInventoryQuery.html', {'allProfiles':allProfiles, 'allColours':allColours})

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

def admin(request):
    return reverse('admin:index')
