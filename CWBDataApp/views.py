from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.db import connection
import pandas as pd
import os
from datetime import date

from .models import Batchcosttracking, Materialcost, Materialinventory, Materialtesting, Ordersheetmachine1, Ordersheetmachine2, Ordersheetmachine3, Picandsum, Productinventory, Productprofiles, Colour

###########################################################HOME PAGE
def index(request):
    return render(request, 'CWBDataApp/index.html')

###########################################################BATCH COST TRACKING
def BatchCostTracking(request):
    allColours = Colour.objects.all()
    allSuppliers= Materialcost.objects.all()

    if request.method == 'POST':

        form = request.POST

        try:
            #Check if batch already exists, if so stop and send an error message
            if Batchcosttracking.objects.get(pk=request.POST['newBatch']):
                return render(request, 'CWBDataApp/BatchCostTracking.html', {'allSuppliers':allSuppliers, 'allColours':allColours, 'error_message' : "Batch already exists, please enter a new batch. If you wish to update a batch talk to an admin",})
        except:

            #Check if any price values are negative, if so return error message
            if float(form['value1']) < 0 or float(form['value2']) < 0 or float(form['value3']) < 0 or float(form['value4']) < 0 or float(form['colourPrice']) < 0 or float(form['foamPrice']) < 0:
                return render(request, 'CWBDataApp/BatchCostTracking.html', {'allSuppliers':allSuppliers, 'allColours':allColours, 'error_message':"Cannot have negative values for prices",})

            if int(form['weight1']) < 0 or int(form['weight2']) < 0 or int(form['weight3']) < 0 or int(form['weight4']) < 0 or int(form['colourWeight']) < 0 or int(form['foamWeight']) < 0:
                return render(request, 'CWBDataApp/BatchCostTracking.html', {'allSuppliers':allSuppliers, 'allColours':allColours, 'error_message':"Cannot have negative values for weights",})
            #Calculate total price, weight and price/pound
            cost = int(form['weight1'])*float(form['value1']) + int(form['weight2'])*float(form['value2']) + int(form['weight3'])*float(form['value3']) + int(form['weight4'])*float(form['value4'])
            cost=round(cost, 2)
            weight = int(form['weight1']) + int(form['weight2']) + int(form['weight3']) + int(form['weight4'])
            #Check if weight was entered as 0, throw error if it is
            if weight == 0:
                return render(request, 'CWBDataApp/BatchCostTracking.html', {'allSuppliers':allSuppliers, 'allColours':allColours, 'error_message':"Total weight cannot be zero, please add a value to weight1",})
            price = round(cost/weight, 2)

            #Check if supplier1 exists before grabbing object
            try:
                sup1_object = Materialcost.objects.get(pk=form['supplier1'])
            except:
                return render(request, 'CWBDataApp/BatchCostTracking.html', {'allSuppliers':allSuppliers, 'allColours':allColours, 'error_message':"Supplier 1 is not a valid supplier",})

            #Check if supplier2 exists before grabbing object
            try:
                if form['supplier2'] == '':
                    sup2_object =  Materialcost.objects.get(pk='None')
                else:
                    sup2_object =  Materialcost.objects.get(pk=form['supplier2'])
            except:
                return render(request, 'CWBDataApp/BatchCostTracking.html', {'allSuppliers':allSuppliers, 'allColours':allColours, 'error_message':"Supplier 2 is not a valid supplier",})

            #Check if supplier3 exists before grabbing object
            try:
                if form['supplier3'] == '':
                    sup3_object =  Materialcost.objects.get(pk='None')
                else:
                    sup3_object =  Materialcost.objects.get(pk=form['supplier3'])
            except:
                return render(request, 'CWBDataApp/BatchCostTracking.html', {'allSuppliers':allSuppliers, 'allColours':allColours, 'error_message':"Supplier 3 is not a valid supplier",})

            #Check if supplier4 exists before grabbing object
            try:
                if form['supplier4'] == '':
                    sup4_object =  Materialcost.objects.get(pk='None')
                else:
                    sup4_object =  Materialcost.objects.get(pk=form['supplier4'])
            except:
                return render(request, 'CWBDataApp/BatchCostTracking.html', {'allSuppliers':allSuppliers, 'allColours':allColours, 'error_message':"Supplier 4 is not a valid supplier",})

            #Create new batch entry
            batch = Batchcosttracking(batchname=form['newBatch'].upper(),
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
            return render(request, 'CWBDataApp/BatchCostTracking.html', {'allSuppliers':allSuppliers, 'allColours':allColours, 'dataAcceptedMessage':"Test Successfully Submitted"})


    return render(request, 'CWBDataApp/BatchCostTracking.html', {'allSuppliers':allSuppliers, 'allColours':allColours})

###########################################################BATCH COST TRACKING QUERY
def BatchCostQuery(request):

    if request.method == 'POST':
        form = request.POST
        try:
            #Grab batch if it exists, throw error if it doesn't
            batch = Batchcosttracking.objects.get(pk=form['searchBatch'].upper())
            #Grab all supplier values
            sup1_object = batch.supplier1.supplier
            sup2_object = batch.supplier2.supplier
            sup3_object = batch.supplier3.supplier
            sup4_object = batch.supplier4.supplier
            return render(request, 'CWBDataApp/BatchCostQuery.html', {'batch' : batch, 'sup1':sup1_object, 'sup2':sup2_object, 'sup3':sup3_object, 'sup4':sup4_object, })
        except:
            return render(request, 'CWBDataApp/BatchCostQuery.html', {'error_message' : "Batch does not exist, please enter a valid batch",})
    return render(request, 'CWBDataApp/BatchCostQuery.html')

###########################################################Batch Cost Excel File Download
def BatchCostExcel(request):
    query = str(Batchcosttracking.objects.all().query)
    df = pd.read_sql_query(query, connection)
    today = str(date.today())

    df.to_excel(r'./CWBDataApp/BatchCostTracking.xlsx', index=False)

    with open(r'./CWBDataApp/BatchCostTracking.xlsx', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = 'attachment; filename=BatchCostTracking-'+today+'.xlsx'
    os.remove(r'./CWBDataApp/BatchCostTracking.xlsx')
    return response

    return render(request, 'CWBDataApp/BatchCostQuery.html')

###########################################################MATERIAL TESTING
def MaterialTesting(request):
    allProfiles= Productprofiles.objects.all()

    if request.method == 'POST':

        form = request.POST

        try:
            Batchcosttracking.objects.get(pk=form['testName'].upper())
        except:
            return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles, 'error_message' : "Batch doesn't exist, please enter a batch first before entering a test.",})

        try:
            testName = Batchcosttracking.objects.get(pk=form['testName'].upper())
            Materialtesting.objects.get(testname=testName, testnumber=int(form['testNum']))
            return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles, 'error_message' : "Test number is already used for this batch, please choose a different test number",})
        except:
            if int(form['timeUsed']) == 1:
                costofmaterial=150
                costoflabour=100
            elif int(form['timeUsed']) == 2:
                costofmaterial=200
                costoflabour=200
            elif int(form['timeUsed']) == 3:
                costofmaterial=400
                costoflabour=300
            elif int(form['timeUsed']) == 4:
                costofmaterial=450
                costoflabour=300
            elif int(form['timeUsed']) == 5:
                costofmaterial=500
                costoflabour=300
            elif int(form['timeUsed']) == 6:
                costofmaterial=600
                costoflabour=350
            elif int(form['timeUsed']) == 8:
                costofmaterial=900
                costoflabour=400
            else:
                costofmaterial=1200
                costoflabour=600

            totalcost = costoflabour + costofmaterial
            testName = Batchcosttracking.objects.get(pk=form['testName'].upper())

            test=Materialtesting(projectnumber=form['projNum'],
                                 testname=testName,
                                 testnumber=form['testNum'],
                                 testdate=form['testDate'],
                                 labourused=form['labourUsed'],
                                 machinetimeused=form['timeUsed'],
                                 productionline=form['productionLine'],
                                 materialstested=form['materialTested'],
                                 othermaterialstested=form['othermaterialTested'],
                                 moulds=form['moulds'],
                                 reasonfortest=form['reasonFor'],
                                 expectedresults=form['expectedResult'],
                                 difficultiesencountered=form['difficulties'],
                                 nextstep=form['nextStep'],
                                 estimatedcostofmaterial=costofmaterial,
                                 estimatedcostoflabour=costoflabour,
                                 totalcostoftest=totalcost
                                 )
            test.save()
            return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles, 'dataAcceptedMessage':"Test Successfully Submitted"})
    return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles})

###########################################################MATERIAL TESTING QUERY
def MaterialTestQuery(request):

    if request.method == 'POST':

        form = request.POST

        try:
            test = Batchcosttracking.objects.get(pk=form['testName'].upper())
            testName = test.batchname
            allTests = Materialtesting.objects.filter(testname=test)
            if not allTests:
                return render(request, 'CWBDataApp/MaterialTestQuery.html', {'error_message':"No test exists for this batch"})
            return render(request, 'CWBDataApp/MaterialTestQuery.html', {'allTests':allTests, 'testName':testName})
        except:
            return render(request, 'CWBDataApp/MaterialTestQuery.html', {'error_message':"Batch does not exist, please enter the batch in batch cost tracking"})
    return render(request, 'CWBDataApp/MaterialTestQuery.html')


###########################################################PRODUCT INVENTORY
def ProductInventory(request):

    allProfiles= Productprofiles.objects.all()
    allColours = Colour.objects.all()

    if request.method == 'POST':
        form = request.POST
        prod_object =  Productprofiles.objects.get(pk=form['prodName'])
        if Productinventory.objects.filter(productname=prod_object, colour=form['colour']).exists():

            return render(request, 'CWBDataApp/ProductInventory.html', {'allProfiles':allProfiles, 'allColours':allColours, 'error_message' : "Product already exists in database, please enter a new product. If you wish to update a product scroll down",})
        elif form['numSkids'] == '' or int(form['numSkids']) <= 0:
            return render(request, 'CWBDataApp/ProductInventory.html', {'allProfiles':allProfiles, 'allColours':allColours, 'error_message' : "Cannot enter a product with zero skids",})
        else:
            newProd = Productinventory(productname=prod_object,
                                       colour=form['colour'],
                                       embossed=form['embossed'],
                                       doublesided=form['doubleSide'],
                                       numberofskids=form['numSkids'])
            newProd.save()
            return render(request, 'CWBDataApp/ProductInventory.html', {'allProfiles':allProfiles, 'allColours':allColours, 'dataAcceptedMessage':"Data Successfully Submitted"})
    return render(request, 'CWBDataApp/ProductInventory.html', {'allProfiles':allProfiles, 'allColours':allColours})

###########################################################PRODUCT INVENTORY UPDATE
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

###########################################################PRODUCT INVENTORY QUERY
def ProductInventoryQuery(request):

    allProfiles= Productprofiles.objects.all()
    allColours = Colour.objects.all()

    if request.method == 'POST':
        form = request.POST
        prod_object =  Productprofiles.objects.get(pk=form['prodName'])

        if Productinventory.objects.filter(productname=prod_object, colour=form['colour']).exists():
            prod = Productinventory.objects.get(productname=prod_object, colour=form['colour'])
            return render(request, 'CWBDataApp/ProductInventoryQuery.html', {'allProfiles':allProfiles, 'allColours':allColours, 'product':prod, 'profile':prod_object})
        else:
            return render(request, 'CWBDataApp/ProductInventoryQuery.html', {'allProfiles':allProfiles, 'allColours':allColours, 'error_message':"This product currently does not exist in inventory. If you wish to enter its data, press the link above"})
    return render(request, 'CWBDataApp/ProductInventoryQuery.html', {'allProfiles':allProfiles, 'allColours':allColours})

###########################################################MATERIAL INVENTORY
def MaterialInventory(request):

    allSuppliers= Materialcost.objects.all()

    if request.method == 'POST':
        form = request.POST

        try:
            Materialinventory.objects.get(pk=form['matName'])
            return render(request, 'CWBDataApp/MaterialInventory.html',{'allSuppliers':allSuppliers, 'error_message':"Material already exists in inventory, if you wish to update its data click the link above"})
        except:
            try:
                if form['numBoxes'] == '' or int(form['numBoxes']) <= 0 or int(form['price'] < 0):
                    return render(request, 'CWBDataApp/MaterialInventory.html',{'allSuppliers':allSuppliers, 'error_message':"Cannot enter zero for number of boxes"})

                sup_object = Materialcost.objects.get(pk=form['supplier'])
                new_material = Materialinventory(materialname=form['matName'].upper(),
                                                 supplier=sup_object,
                                                 numberofboxes=form['numBoxes'],
                                                 locations=form['location'],
                                                 premixed=form['premixed'],
                                                 priceperpound=(form['price']))
                new_material.save()
                return render(request, 'CWBDataApp/MaterialInventory.html', {'allSuppliers':allSuppliers, 'dataAcceptedMessage':"Material Successfully Added",})
            except:
                return render(request, 'CWBDataApp/MaterialInventory.html',{'allSuppliers':allSuppliers, 'error_message':"Supplier does not exist"})


    return render(request, 'CWBDataApp/MaterialInventory.html', {'allSuppliers':allSuppliers})

###########################################################MATERIAL INVENTORY QUERY
##Fucking broken
def MaterialInventoryQuery(request):

    if request.method == 'POST':
        form = request.POST
        try:
            if form['matName'].upper() == 'ALL':
                all_materials = Materialinventory.objects.all()
                return render(request, 'CWBDataApp/MaterialInventoryQuery.html', {'all_materials':all_materials})


            mat_object =  Materialinventory.objects.filter(pk=form['matName'].upper())
            return render(request, 'CWBDataApp/MaterialInventoryQuery.html', {'all_materials':mat_object})
        except:
            return render(request, 'CWBDataApp/MaterialInventoryQuery.html', {'error_message':"This material currently does not exist in inventory. If you wish to enter its data, press the link above"})

    return render(request, 'CWBDataApp/MaterialInventoryQuery.html')

###########################################################MATERIAL INVENTORY QUERY
def MaterialInventoryUpdate(request):

    if request.method == 'POST':
        form = request.POST
        try:
            mat_object =  Materialinventory.objects.get(pk=form['matName'].upper())

            return render(request, 'CWBDataApp/MaterialInventoryUpdate.html', {'material':mat_object})
        except:
            return render(request, 'CWBDataApp/MaterialInventoryUpdate.html', {'error_message':"This material currently does not exist in inventory. If you wish to enter its data, press the link above"})


    return render(request, 'CWBDataApp/MaterialInventoryUpdate.html')

###########################################################ORDER SHEET MACHINE 1
def OrderSheetsMachine1(request):
    return render(request, 'CWBDataApp/OrderSheetsMachine1.html')

###########################################################ORDER SHEET MACHINE 2
def OrderSheetsMachine2(request):
    return render(request, 'CWBDataApp/OrderSheetsMachine2.html')

###########################################################ORDER SHEET MACHINE 3
def OrderSheetsMachine3(request):
    return render(request, 'CWBDataApp/OrderSheetsMachine3.html')

###########################################################HELP
def help(request):
    return render(request, 'CWBDataApp/help.html')

###########################################################Add Employee
def AddEmployee(request):
    return render(request, 'CWBDataApp/AddEmployee.html')

###########################################################Add Board Profile
def AddBoardProfile(request):
    return render(request, 'CWBDataApp/AddBoardProfile.html')

###########################################################Add Colour
def AddColour(request):
    return render(request, 'CWBDataApp/AddColour.html')

###########################################################Add Supplier
def AddSupplier(request):
    return render(request, 'CWBDataApp/AddSupplier.html')

###########################################################Add Supplier
def UpdateSupplier(request):
    return render(request, 'CWBDataApp/UpdateSupplier.html')


###########################################################ADMIN
def admin(request):
    return reverse('admin:index')
