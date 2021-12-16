from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.db import connection
import pandas as pd
import os
from datetime import date, timedelta
from decimal import Decimal
import math

from .models import Batchcosttracking, Batchcost, Materialcost, Materialinventory, Materialtesting, Ordersheetmachine1, Ordersheetmachine2, Ordersheetmachine3, Picandsum, Productinventory, Productprofiles, Colour, Employees, Profileaverages

###########################################################HOME PAGE
def index(request):
    return render(request, 'CWBDataApp/index.html')

###########################################################BATCH COST TRACKING
def BatchCostTracking(request):
    allColours = Colour.objects.all()
    allMaterials= Materialinventory.objects.all()
    num_of_materials = 11

    if request.method == 'POST':

        form = request.POST

        try:
            #Check if batch already exists, if so stop and send an error message
            if Batchcost.objects.get(pk=request.POST['newBatch']):
                return render(request, 'CWBDataApp/BatchCostTracking.html', {'allMaterials':allMaterials, 'allColours':allColours, 'range':range(1, num_of_materials), 'error_message' : "Batch already exists, please enter a new batch. If you wish to update a batch talk to an admin",})
        except:

            #Calculate total price, weight and price/pound
            cost = 0
            weight = 0
            for i in range(1, num_of_materials):
                cost += int(form['weight'+ str(i)]) * Decimal(form['value'+str(i)])
            cost += (Decimal(form['colourWeight']) * Decimal(form['colourPrice'])) + (Decimal(form['foamWeight']) * Decimal(form['foamPrice']))
            cost=round(cost, 2)

            for i in range(1, num_of_materials):
                weight += int(form['weight'+str(i)])
            weight += Decimal(form['colourWeight']) + Decimal(form['foamWeight'])
            #Check if weight was entered as 0, throw error if it is
            if weight == 0:
                return render(request, 'CWBDataApp/BatchCostTracking.html', {'allMaterials':allMaterials, 'allColours':allColours, 'range':range(1, num_of_materials), 'error_message':"Total weight cannot be zero, please add a value to weight1",})

            price = round(cost/weight, 2)

            #Check if theres enough boxes before we subtract from inventory
            for i in range(1, num_of_materials):
                try:
                    if form['material'+str(i)] != 'None':
                        box = Materialinventory.objects.get(pk=form['material'+str(i)])

                        if box.numberofboxes < Decimal(form['numofBoxes'+str(i)]):
                            return render(request, 'CWBDataApp/BatchCostTracking.html', {'allMaterials':allMaterials, 'allColours':allColours, 'range':range(1, num_of_materials), 'error_message' : form["material"+str(i)]+" does no have enough boxes for Material"+str(i)+"",})
                except:
                    return render(request, 'CWBDataApp/BatchCostTracking.html', {'allMaterials':allMaterials, 'allColours':allColours, 'range':range(1, num_of_materials), 'error_message' : "Couldn't find box in inventory",})

            for i in range(1, num_of_materials):
                try:
                    if form['material'+str(i)] != 'None':
                        box = Materialinventory.objects.get(pk=form['material'+str(i)])
                        box.numberofboxes -= Decimal(form['numofBoxes'+str(i)])
                        box.save()
                        if box.numberofboxes <=0:
                            box.delete()
                except:
                    return render(request, 'CWBDataApp/BatchCostTracking.html', {'allMaterials':allMaterials, 'allColours':allColours, 'range':range(1, num_of_materials), 'error_message' : form["material"+str(i)]+" does not have enough boxes for Material"+str(i)+"",})

            #Create new batch entry
            batch = Batchcost(batchname=form['newBatch'].upper(),
                                    batchdate=form['batchDate'],
                                    totalcost=cost,
                                    totalweight=weight,
                                    priceperpound=price,
                                    material1=form['material1'],
                                    weight1=form['weight1'],
                                    value1=form['value1'],
                                    material2=form['material2'],
                                    weight2=form['weight2'],
                                    value2=form['value2'],
                                    material3=form['material3'],
                                    weight3=form['weight3'],
                                    value3=form['value3'],
                                    material4=form['material4'],
                                    weight4=form['weight4'],
                                    value4=form['value4'],
                                    material5=form['material5'],
                                    weight5=form['weight5'],
                                    value5=form['value5'],
                                    material6=form['material6'],
                                    weight6=form['weight6'],
                                    value6=form['value6'],
                                    material7=form['material7'],
                                    weight7=form['weight7'],
                                    value7=form['value7'],
                                    material8=form['material8'],
                                    weight8=form['weight8'],
                                    value8=form['value8'],
                                    material9=form['material9'],
                                    weight9=form['weight9'],
                                    value9=form['value9'],
                                    material10=form['material10'],
                                    weight10=form['weight10'],
                                    value10=form['value10'],
                                    colour=form['colour'],
                                    colourweight=form['colourWeight'],
                                    colourvalue=form['colourPrice'],
                                    foamweight=form['foamWeight'],
                                    foamvalue=form['foamPrice'],
                                    totalshredweight=form['shredWeight']
                                    )
            batch.save()
            return render(request, 'CWBDataApp/BatchCostTracking.html', {'allMaterials':allMaterials, 'allColours':allColours, 'range':range(1, num_of_materials), 'dataAcceptedMessage':"Batch Successfully Submitted and material used removedd from inventory"})


    return render(request, 'CWBDataApp/BatchCostTracking.html', {'allMaterials':allMaterials, 'allColours':allColours, 'range':range(1, num_of_materials)})

###########################################################BATCH COST TRACKING QUERY
def BatchCostQuery(request):

    if request.method == 'POST':
        form = request.POST
        #Number of material boxes that are allowed to be entered
        num_of_materials = 11

        #try:
            #Grab batch if it exists, throw error if it doesn't
        batch = Batchcost.objects.get(pk=form['searchBatch'].upper())
        dict= {}
        for i in range(1, num_of_materials):
            dict['material'+str(i)] = getattr(batch, 'material'+str(i))
            dict['weight'+str(i)] = getattr(batch, 'weight'+str(i))
            dict['value'+str(i)] = getattr(batch, 'value'+str(i))
        return render(request, 'CWBDataApp/BatchCostQuery.html', {'batch' : batch, 'range':range(1,num_of_materials), 'dict':dict.items(),})
        #except:
            #return render(request, 'CWBDataApp/BatchCostQuery.html', {'error_message' : "Batch does not exist, please enter a valid batch",})
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
    allEmployees= Employees.objects.all()

    if request.method == 'POST':

        form = request.POST

        try:
            Batchcosttracking.objects.get(pk=form['testName'].upper())
        except:
            return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles, 'allEmployees':allEmployees, 'error_message' : "Batch doesn't exist, please enter a batch first before entering a test.",})

        try:
            testName = Batchcosttracking.objects.get(pk=form['testName'].upper())
            Materialtesting.objects.get(testname=testName, testnumber=int(form['testNum']))
            return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles, 'allEmployees':allEmployees, 'error_message' : "Test number is already used for this batch, please choose a different test number",})
        except:
            if int(form['machinetimeUsed']) == 1:
                costofmaterial=150
                costoflabour=100
            elif int(form['machinetimeUsed']) == 2:
                costofmaterial=200
                costoflabour=200
            elif int(form['machinetimeUsed']) == 3:
                costofmaterial=400
                costoflabour=300
            elif int(form['machinetimeUsed']) == 4:
                costofmaterial=450
                costoflabour=300
            elif int(form['machinetimeUsed']) == 5:
                costofmaterial=500
                costoflabour=300
            elif int(form['machinetimeUsed']) == 6:
                costofmaterial=600
                costoflabour=350
            elif int(form['machinetimeUsed']) == 8:
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
                                 machinetimeused=form['machinetimeUsed'],
                                 productionline=form['productionLine'],
                                 materialstested=form['materialsTested'],
                                 othermaterialstested=form['othermaterialsTested'],
                                 moulds=form['moulds'],
                                 reasonfortest=form['reasonForTest'],
                                 expectedresults=form['expectedResults'],
                                 difficultiesencountered=form['difficultiesencountered'],
                                 nextstep=form['nextStep'],
                                 estimatedcostofmaterial=costofmaterial,
                                 estimatedcostoflabour=costoflabour,
                                 totalcostoftest=totalcost
                                 )
            test.save()
            return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles, 'allEmployees':allEmployees, 'dataAcceptedMessage':"Test Successfully Submitted"})
    return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles, 'allEmployees':allEmployees})

###########################################################MATERIAL TESTING Populate
def MaterialTestingPopulate(request):
    allProfiles= Productprofiles.objects.all()

    if request.method == 'POST':

        form = request.POST

        if int(form['testNum']) > 1:
            try:
                Batchcosttracking.objects.get(pk=form['testName'].upper())
            except:
                return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles, 'error_message' : "Batch doesn't exist, please enter a batch first before entering a test.",})

            try:
                testName = Batchcosttracking.objects.get(pk=form['testName'].upper())
                Materialtesting.objects.get(testname=testName, testnumber=int(form['testNum']))
                return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles, 'error_message' : "Test number is already used for this batch, please choose a different test number",})
            except:

                testName = Batchcosttracking.objects.get(pk=form['testName'].upper())
                prev_test = Materialtesting.objects.get(testname=testName, testnumber=int(form['testNum'])-1)

                pop_data = {}
                entered_data = {}
                for key, value in form.items():
                    if value == '':
                        pop_data[key.lower()] = getattr(prev_test, key.lower())
                    else:
                        entered_data[key.lower()] = value
                return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles, 'dataAcceptedMessage':"Data Populated", 'pop_data':pop_data, 'entered_data':entered_data})

                return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles, 'error_message' : "Something went wrong, can't populate data",})
        else:
            return render(request, 'CWBDataApp/MaterialTesting.html', {'allProfiles':allProfiles, 'error_message':"Cannot populate data on the first test"})
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
        if Productinventory.objects.filter(productname=form['prodName'], colour=form['colour']).exists():

            return render(request, 'CWBDataApp/ProductInventory.html', {'allProfiles':allProfiles, 'allColours':allColours, 'error_message' : "Product already exists in database, please enter a new product. If you wish to update a product scroll down",})
        elif form['numSkids'] == '' or int(form['numSkids']) <= 0:
            return render(request, 'CWBDataApp/ProductInventory.html', {'allProfiles':allProfiles, 'allColours':allColours, 'error_message' : "Cannot enter a product with zero skids",})
        else:
            orderDict = FindOrder(form['prodName'], form['colour'])
            UpdateOrderInventory(orderDict.order, int(form['numSkids']), orderDict.orderSheet)

            newProd = Productinventory(productname=form['prodName'],
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

        if Productinventory.objects.filter(productname=form['prodName'], colour=form['colour']).exists():
            prod_object = Productinventory.objects.get(productname=form['prodName'], colour=form['colour'])
            return render(request, 'CWBDataApp/ProductInventoryUpdate.html', {'allProfiles':allProfiles, 'allColours':allColours, 'Forms':True, 'prod_object':prod_object})
        else:
            return render(request, 'CWBDataApp/ProductInventoryUpdate.html', {'allProfiles':allProfiles, 'allColours':allColours, 'error_message':"This product currently does not exist in inventory. If you wish to enter its data, press the link above"})
    return render(request, 'CWBDataApp/ProductInventoryUpdate.html', {'allProfiles':allProfiles, 'allColours':allColours})

###########################################################PRODUCT INVENTORY UPDATE SKIDS
def ProductInventoryUpdateSkids(request):
    allProfiles= Productprofiles.objects.all()
    allColours = Colour.objects.all()

    if request.method == 'POST':
        form = request.POST

        if Productinventory.objects.filter(productname=form['prodName'], colour=form['colour']).exists() and int(form['numSkids']) >= 0:
            prod = Productinventory.objects.get(productname=form['prodName'], colour=form['colour'])

            differenceInPieces = int(form['numSkids']) - prod.numberofskids
            orderDict = FindOrder(form['prodName'], form['colour'])
            UpdateOrderInventory(orderDict.get('order'), differenceInPieces, orderDict.get('orderSheet'))

            if int(form['numSkids']) == 0:
                prod.delete()
                return render(request, 'CWBDataApp/ProductInventoryUpdate.html', {'allProfiles':allProfiles, 'allColours':allColours, 'dataAcceptedMessage':"Product Successfully Deleted Since No Skids Remain"})
            else:
                prod.numberofskids = int(form['numSkids'])
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

        if Productinventory.objects.filter(productname=form['prodName'], colour=form['colour']).exists():
            prod = Productinventory.objects.get(productname=form['prodName'], colour=form['colour'])
            return render(request, 'CWBDataApp/ProductInventoryQuery.html', {'allProfiles':allProfiles, 'allColours':allColours, 'product':prod})
        else:
            return render(request, 'CWBDataApp/ProductInventoryQuery.html', {'allProfiles':allProfiles, 'allColours':allColours, 'error_message':"This product currently does not exist in inventory. If you wish to enter its data, press the link above"})
    return render(request, 'CWBDataApp/ProductInventoryQuery.html', {'allProfiles':allProfiles, 'allColours':allColours})

###########################################################PRODUCT INVENTORY SHIPPED
def ProductInventoryShipped(request):

    allProfiles= Productprofiles.objects.all()
    allColours = Colour.objects.all()

    if request.method == 'POST':
        form = request.POST

        if Productinventory.objects.filter(productname=form['prodName'], colour=form['colour']).exists():
            prod = Productinventory.objects.get(productname=form['prodName'], colour=form['colour'])

            PiecesRemaining = prod.numberofskids - int(form['numSkids'])

            orderDict = FindOrder(form['prodName'], form['colour'])
            updateOrderSent(orderDict.order, int(form['numSkids']), orderDict.orderSheet)

            if PiecesRemaining <= 0:
                prod.delete()
                PiecesRemaining = 0
            else:
                prod.numberofskids = PiecesRemaining
                prod.save()
            return render(request, 'CWBDataApp/ProductInventoryShipped.html', {'allProfiles':allProfiles, 'allColours':allColours, 'dataAcceptedMessage':"Number of Skids Successfully Updated", 'skids':str(PiecesRemaining)})
        else:
            return render(request, 'CWBDataApp/ProductInventoryShipped.html', {'allProfiles':allProfiles, 'allColours':allColours, 'error_message':"This product currently does not exist in inventory. If you wish to enter its data, press the link above"})
    return render(request, 'CWBDataApp/ProductInventoryShipped.html', {'allProfiles':allProfiles, 'allColours':allColours})

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
                if form['numBoxes'] == '' or float(form['numBoxes']) <= 0 or float(form['price']) < 0:
                    return render(request, 'CWBDataApp/MaterialInventory.html',{'allSuppliers':allSuppliers, 'error_message':"Cannot enter zero for number of boxes or price"})

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

###########################################################MATERIAL INVENTORY UPDATE
def MaterialInventoryUpdate(request):

    if request.method == 'POST':
        form = request.POST
        try:
            if Materialinventory.objects.get(pk=form['matName'].upper()):
                mat_object = Materialinventory.objects.get(pk=form['matName'].upper())
                return render(request, 'CWBDataApp/MaterialInventoryUpdate.html', {'Forms':True, 'Material':mat_object})
            else:
                return render(request, 'CWBDataApp/MaterialInventoryUpdate.html', {'error_message':"Material does not exist in inventory, check your spelling"})

        except:
            return render(request, 'CWBDataApp/MaterialInventoryUpdate.html', {'error_message':"This material currently does not exist in inventory. If you wish to enter its data, press the link above"})


    return render(request, 'CWBDataApp/MaterialInventoryUpdate.html')

###########################################################MATERIAL INVENTORY UPDATE NUMBER of SKIDS
def MaterialInventoryUpdateNumSkids(request):

    if request.method == 'POST':
        form = request.POST
        try:
            if form['numBoxes'] == '' or float(form['numBoxes']) < 0 or float(form['price']) < 0:
                return render(request, 'CWBDataApp/MaterialInventoryUpdate.html',{'error_message':"Cannot enter zero for number of boxes"})
            elif float(form['numBoxes']) == 0:
                mat_object = Materialinventory.objects.get(pk=form['matName'].upper())
                mat_object.delete()
                return render(request, 'CWBDataApp/MaterialInventoryUpdate.html', {'dataAcceptedMessage':"Material Was Successfully Deleted Since Zero Boxes Remained"})

            mat_object = Materialinventory.objects.get(pk=form['matName'].upper())
            mat_object.numberofboxes = form['numBoxes']
            mat_object.locations = form['location']
            mat_object.priceperpound = form['price']
            mat_object.save()
            return render(request, 'CWBDataApp/MaterialInventoryUpdate.html', {'dataAcceptedMessage':"Material Updated"})
        except:
            return render(request, 'CWBDataApp/MaterialInventoryUpdate.html', {'error_message':"Could not update material, try again"})


    return render(request, 'CWBDataApp/MaterialInventoryUpdate.html')

###########################################################ORDER SHEET MACHINE 1
def OrderSheetsMachine1(request):
    allColours = Colour.objects.all()
    allProfiles= Productprofiles.objects.all()

    if request.method == 'POST':
        form = request.POST

        pcsinventorized = 0

        if Productinventory.objects.filter(productname=form['prodName'], colour=form['colour']).exists() and Ordersheetmachine1.objects.filter(boardprofile=form['prodName'], colour=form['colour']).exists() == False:
            product = Productinventory.objects.filter(productname=form['prodName'], colour=form['colour']).first()
            pcsinventorized = int(product.numberofskids)

        product = Productprofiles.objects.get(pk=form['prodName'])
        productAverage = Profileaverages.objects.get(pk=form['prodName'])
        pcsremaining = int(form['pcs']) - int(form['pcsSent']) - pcsinventorized
        skidsremaining = pcsremaining / int(product.pcsperskid)
        lengthofrunindays = Decimal(skidsremaining) / Decimal(productAverage.averageskidsperday)
        priority = 0
        startdate = date.today()
        enddate = startdate + timedelta(days=math.ceil(lengthofrunindays))
        duedate = enddate
        ponumber = form['ponumber']

        if Ordersheetmachine1.objects.all() == None:
            priority = 1
        else:
            if form['priority'] == '' :
                #If no priority is given, grab the lowest priority entry and give this order a lower priority
                lastOrder = Ordersheetmachine1.objects.all().order_by('-priorityrank').first()
                priority = lastOrder.priorityrank + 1
                startdate = lastOrder.projectedenddate
                enddate = startdate + timedelta(days=math.ceil(lengthofrunindays))


            else:
                lessPriority = Ordersheetmachine1.objects.filter(priorityrank__gt = (int(form['priority'])-1)).order_by('priorityrank')
                if int(form['priority']) == 1:
                    startdate = date.today()
                else:
                    higherpriority = Ordersheetmachine1.objects.filter(priorityrank=(int(form['priority'])-1)).first()
                    startdate = higherpriority.projectedenddate
                enddate = startdate + timedelta(days=math.ceil(lengthofrunindays))
                deprioritize(form['priority'], enddate, lessPriority)
                priority = form['priority']

        if form['dueDate'] == '':
            duedate = enddate
        else:
            duedate = form['dueDate']

        newOrder=Ordersheetmachine1( customerponumber=ponumber,
                                      projectedstartdate=startdate,
                                      projectedenddate=enddate,
                                      duedate=duedate,
                                      lengthofrunindays=lengthofrunindays,
                                      priorityrank=priority,
                                      boardprofile=form['prodName'],
                                      colour=form['colour'],
                                      skidsremaining=skidsremaining,
                                      pcs=form['pcs'],
                                      pcssent=form['pcsSent'],
                                      pcsremaining=pcsremaining,
                                      customer=form['customer'],
                                      qualitynotes=form['qualitynotes'],
                                      pcsinventorized=pcsinventorized)
        newOrder.save()
        return render(request, 'CWBDataApp/OrderSheetsMachine1.html', {'allColours':allColours, 'allProfiles':allProfiles, 'dataAcceptedMessage':"Order Successfully Added"})
    return render(request, 'CWBDataApp/OrderSheetsMachine1.html', {'allColours':allColours, 'allProfiles':allProfiles})

#Helper method to rearrange the priority and dates of orders
def deprioritize(priority, endDate, querySet):

    for entry in querySet:
        if entry.priorityrank == priority:
            entry.projectedstartdate = endDate
            entry.projectedenddate = endDate + timedelta(days=math.ceil(entry.lengthofrunindays))
        else:
            higherpriority = querySet.filter(priorityrank=entry.priorityrank).first()
            entry.projectedstartdate = higherpriority.projectedenddate
            entry.projectedenddate =  higherpriority.projectedenddate + timedelta(days=math.ceil(entry.lengthofrunindays))
        entry.priorityrank += 1
        entry.save()

#Helper method to update orders when product is shipped
def updateOrderSent(order, pcsSent):

    order.pcssent += pcsSent
    order.pcsinventorized -= pcsSent
    order.save()


    if order.pcssent >= order.pcs:
        deletedOrder(order, orderSheet)
        order.delete()

#Given a Product and colour, find the Ordersheet that and order that needs that product
#Return the specific order and ordersheet for that product
def FindOrder(product, colour):
    dict = {}
    if Ordersheetmachine1.objects.filter(boardprofile=product, colour=colour).exists():
        dict['order'] = Ordersheetmachine1.objects.filter(boardprofile=product, colour=colour).order_by('priorityrank').first()
        dict['orderSheet'] = Ordersheetmachine1.objects.all()
    elif Ordersheetmachine2.objects.filter(boardprofile=product, colour=colour).exists():
        dict['order'] = Ordersheetmachine2.objects.filter(boardprofile=product, colour=colour).order_by('priorityrank').first()
        dict['orderSheet'] = Ordersheetmachine2.objects.all()
    elif Ordersheetmachine3.objects.filter(boardprofile=product, colour=colour).exists():
        dict['order'] = Ordersheetmachine3.objects.filter(boardprofile=product, colour=colour).order_by('priorityrank').first()
        dict['orderSheet'] = Ordersheetmachine3.objects.all()
    return dict

#Update an orders inventorized pieces
def UpdateOrderInventory(order, pcsinventorized, orderSheet):
    order.pcsinventorized += pcsinventorized
    order.pcsremaining -= pcsinventorized
    order.save()
    if order.pcs <= 0:
        deletedOrder(order, orderSheet)
        order.delete()

#Reorder orders when an order needs to be deleted
def deletedOrder(order, orderSheet):
    endDate = date.today()
    if order.priorityrank != 1:
        higherOrder = orderSheet.filter(priorityrank=(order.priorityrank -1)).first()
        endDate = higherOrder.projectedenddate
    lowerOrder = orderSheet.filter(priorityrank__gt=order.priorityrank)

    #Change projected start and end dates based on which order was removed, update priority by 1
    for item in lowerOrder:
            item.projectedstartdate = endDate
            item.projectedenddate = endDate + timedelta(days=math.ceil(item.lengthofrunindays))
            item.priorityrank -= 1
            item.save()
            endDate = item.projectedenddate

###########################################################ORDER SHEET MACHINE 2
def OrderSheetsMachine2(request):
    return render(request, 'CWBDataApp/OrderSheetsMachine2.html')

###########################################################ORDER SHEET MACHINE 3
def OrderSheetsMachine3(request):
    return render(request, 'CWBDataApp/OrderSheetsMachine3.html')

###########################################################ORDER SHEET MACHINE 3
def ViewOrders(request):
    #Number of machine options to be displayed on page
    numberOfMachines = 3

    if request.method == 'POST':
        form = request.POST
        dict = {}

        if form['machine'] == '1':
            if Ordersheetmachine1.objects.all():
                dict['machine1'] = Ordersheetmachine1.objects.all().order_by('priorityrank')
        elif form['machine'] == '2':
            if Ordersheetmachine2.objects.all():
                dict['machine2'] = Ordersheetmachine2.objects.all().order_by('priorityrank')
        elif form['machine'] == '3':
            if Ordersheetmachine3.objects.all():
                dict['machine3'] = Ordersheetmachine3.objects.all().order_by('priorityrank')
        elif form['machine'] == 'all':
            dict['machine1'] = Ordersheetmachine1.objects.all().order_by('priorityrank')
            dict['machine2'] = Ordersheetmachine2.objects.all().order_by('priorityrank')
            dict['machine3'] = Ordersheetmachine3.objects.all().order_by('priorityrank')

        if not dict:
            return render(request, 'CWBDataApp/ViewOrders.html', {'numberOfMachines':range(1, numberOfMachines+1), 'error_message': "There are Currently No Orders For This Machine"})
        else:
            return render(request, 'CWBDataApp/ViewOrders.html', {'numberOfMachines':range(1, numberOfMachines+1), 'allOrders':dict.values()})

    return render(request, 'CWBDataApp/ViewOrders.html', {'numberOfMachines':range(1, numberOfMachines+1)})


###########################################################UPDATE ORDERS
def UpdateOrders(request):
    #Number of machine options to be displayed on page
    numberOfMachines = 3

    if request.method == 'POST':
        form = request.POST
        orders = None
        machine = 1

        if form['machine'] == '1':
            if Ordersheetmachine1.objects.all():
                orders = Ordersheetmachine1.objects.all().order_by('priorityrank')
        elif form['machine'] == '2':
            if Ordersheetmachine2.objects.all():
                orders = Ordersheetmachine2.objects.all().order_by('priorityrank')
            machine = 2
        elif form['machine'] == '3':
            if Ordersheetmachine3.objects.all():
                orders = Ordersheetmachine3.objects.all().order_by('priorityrank')
            machine = 3
        if orders == None:
            return render(request, 'CWBDataApp/UpdateOrders.html', {'numberOfMachines':range(1, numberOfMachines+1), 'error_message':"No Orders Exist For This Machine"})
        else:
            return render(request, 'CWBDataApp/UpdateOrders.html', {'numberOfMachines':range(1, numberOfMachines+1), 'orders':orders, 'machine':machine})

    return render(request, 'CWBDataApp/UpdateOrders.html', {'numberOfMachines':range(1, numberOfMachines+1)})

###########################################################GET SPECIFIC ORDER TO UPDATE
def GetOrder(request):
    #Number of machine options to be displayed on page
    numberOfMachines = 3

    if request.method == 'POST':
        form = request.POST

        try:
            orderModel = globals()["Ordersheetmachine" + form['machine']]
            order = orderModel.objects.get(priorityrank=form['orderrank'])
            return render(request, 'CWBDataApp/UpdateOrders.html', {'numberOfMachines':range(1, numberOfMachines+1), 'orderChange':order, 'machine':form['machine']})
        except:
            return render(request, 'CWBDataApp/UpdateOrders.html', {'numberOfMachines':range(1, numberOfMachines+1), 'error_message':"Could not grab orders"})
    return render(request, 'CWBDataApp/UpdateOrders.html', {'numberOfMachines':range(1, numberOfMachines+1)})

###########################################################Change ORDER
def ChangeOrder(request):
    #Number of machine options to be displayed on page
    numberOfMachines = 3

    if request.method == 'POST':
        form = request.POST


        orderModel = globals()["Ordersheetmachine" + form['machine']]
        order = orderModel.objects.get(pk=form['orderPK'])
        order.customerponumber = form['ponumber']
        order.customer = form['customer']
        order.qualitynotes = form['qualitynotes']

        if order.pcs != int(form['pcs']):
            order.pcs = form['pcs']
            order.pcsremaining = int(form['pcs']) - order.pcssent - order.pcsinventorized
            product = Productprofiles.objects.get(pk=order.boardprofile)
            productAverage = Profileaverages.objects.get(pk=order.boardprofile)
            order.skidsremaining = order.pcsremaining / int(product.pcsperskid)
            order.lengthofrunindays = order.skidsremaining / Decimal(productAverage.averageskidsperday)
            order.projectedenddate = addDate(order.projectedstartdate, math.ceil(order.lengthofrunindays))
            order.save()
            #Grab all orders with lower priority
            lowerOrders = orderModel.objects.filter(priorityrank__gt=form['priority']).order_by('priorityrank')
            endDate = order.projectedenddate
            for item in lowerOrders:
                item.projectedstartdate = endDate
                item.projectedenddate = addDate(endDate, math.ceil(item.lengthofrunindays))
                item.save()
                endDate = item.projectedenddate


        #If priority was changed then reorder all the order where necessary
        #If new priority is higher than the current, shuffle all orders down
        if int(form['priority']) < order.priorityrank:
            startdate = None
            lessPriority = orderModel.objects.filter(priorityrank__gte = (int(form['priority']))).order_by('priorityrank')
            if int(form['priority']) == 1:
                startdate = date.today()
            else:
                higherpriority = orderModel.objects.filter(priorityrank=(int(form['priority'])-1)).first()
                startdate = higherpriority.projectedenddate
            enddate = addDate(startdate, math.ceil(order.lengthofrunindays))

            #Loop to change priority and dates of order the are under the new priority
            for entry in lessPriority:
                if entry.priorityrank == form['priority']:
                    entry.projectedstartdate = endDate
                    entry.projectedenddate = endDate + timedelta(days=math.ceil(entry.lengthofrunindays))
                else:
                    higherpriority = orderModel.objects.filter(priorityrank=entry.priorityrank).first()
                    entry.projectedstartdate = higherpriority.projectedenddate
                    entry.projectedenddate =  higherpriority.projectedenddate + timedelta(days=math.ceil(entry.lengthofrunindays))
                #only change priority of orders in which the priority was shifted
                if entry.priorityrank < order.priorityrank:
                    entry.priorityrank += 1
                entry.save()

            order.priorityrank = form['priority']
            order.projectedstartdate = startdate
            order.projectedenddate = enddate
            order.save()
        elif int(form['priority']) > order.priorityrank:
            startdate = None
            lessPriority = orderModel.objects.filter(priorityrank__gt = order.priorityrank ).order_by('priorityrank')

            if order.priorityrank == 1:
                startdate = date.today()
            else:
                higherpriority = orderModel.objects.filter(priorityrank=order.priorityrank).first()
                startdate = higherpriority.projectedenddate

            for entry in lessPriority:
                if entry.priorityrank == int(order.priorityrank) + 1:
                    entry.projectedstartdate = startdate
                    entry.projectedenddate = addDate(startdate, math.ceil(entry.lengthofrunindays))
                elif entry.priorityrank > order.priorityrank+1 and entry.priorityrank <= int(form['priority']):
                    higherpriority = orderModel.objects.filter(priorityrank=entry.priorityrank-2).first()
                    entry.projectedstartdate = higherpriority.projectedenddate
                    entry.projectedenddate =  addDate(higherpriority.projectedenddate, math.ceil(entry.lengthofrunindays))
                elif entry.priorityrank > form['priority']:
                    higherpriority = orderModel.objects.filter(priorityrank=entry.priorityrank-1).first()
                    entry.projectedstartdate = higherpriority.projectedenddate
                    entry.projectedenddate =  addDate(higherpriority.projectedenddate, math.ceil(entry.lengthofrunindays))

                if entry.priorityrank == int(form['priority']):
                    order.priorityrank = form['priority']
                    order.projectedstartdate = entry.projectedenddate
                    order.projectedenddate = addDate(entry.projectedenddate, math.ceil(order.lengthofrunindays))
                    order.save()
                #only change priority of orders in which the priority was shifted
                if entry.priorityrank <= int(form['priority']):
                    entry.priorityrank -= 1
                entry.save()

        order.save()

        return render(request, 'CWBDataApp/UpdateOrders.html', {'numberOfMachines':range(1, numberOfMachines+1), 'dataAcceptedMessage':"Order updated"})
    return render(request, 'CWBDataApp/UpdateOrders.html')


###########################################################HELP
def PicSum(request):
    return render(request, 'CWBDataApp/PicSum.html')

###########################################################HELP
def help(request):
    return render(request, 'CWBDataApp/help.html')

###########################################################Add Employee
def AddEmployee(request):

    if request.method == 'POST':
        form = request.POST

        try:
            employee = Employees.objects.get(pk=form['employeeName'])
            return render(request, 'CWBDataApp/AddEmployee.html', {'error_message':"Employee already exists"})
        except:
            new_employee = Employees(employeename=form['employeeName'])
            new_employee.save()
            return render(request, 'CWBDataApp/AddEmployee.html', {'dataAcceptedMessage':"Employee Successfully Added"})
    return render(request, 'CWBDataApp/AddEmployee.html')

###########################################################Remove Employee
def RemoveEmployee(request):

    if request.method == 'POST':
        form = request.POST

        try:
            employee = Employees.objects.get(pk=form['employeeName'])
            employee.delete()
            return render(request, 'CWBDataApp/AddEmployee.html', {'dataAcceptedMessage':"Employee Successfully Removed"})
        except:
            return render(request, 'CWBDataApp/AddEmployee.html', {'error_message':"Employee Cannot Be Removed Because They Do Not Exist"})
    return render(request, 'CWBDataApp/AddEmployee.html')

###########################################################Add Board Profile
def AddBoardProfile(request):

    if request.method == 'POST':
        form = request.POST

        try:
            profile = Productprofiles.objects.get(pk=form['profile'])
            return render(request, 'CWBDataApp/AddBoardProfile.html', {'error_message':"Profile already exists"})
        except:
            new_profile = Productprofiles(productname=form['profile'])
            new_profile.save()
            return render(request, 'CWBDataApp/AddBoardProfile.html', {'dataAcceptedMessage':"Profile Successfully Added"})
    return render(request, 'CWBDataApp/AddBoardProfile.html')

###########################################################Add Board Profile
def RemoveBoardProfile(request):

    if request.method == 'POST':
        form = request.POST

        try:
            if form['profile'] == '':
                return render(request, 'CWBDataApp/AddBoardProfile.html', {'error_message':"Please enter a profile"})
            profile = Productprofiles.objects.get(pk=form['profile'])
            profile.delete()
            return render(request, 'CWBDataApp/AddBoardProfile.html', {'dataAcceptedMessage':"Profile Successfully Removed"} )
        except:
            return render(request, 'CWBDataApp/AddBoardProfile.html', {'error_message':"Profile cannot be removed because it does not exist"})
    return render(request, 'CWBDataApp/AddBoardProfile.html')


###########################################################Add Colour
def AddColour(request):

    if request.method == 'POST':
        form = request.POST

        try:
            colour = Colour.objects.get(pk=form['colour'])
            return render(request, 'CWBDataApp/AddColour.html', {'error_message':"Colour already exists"})
        except:
            new_colour = Colour(colour=form['colour'])
            new_colour.save()
            return render(request, 'CWBDataApp/AddColour.html', {'dataAcceptedMessage':"Colour Successfully Added"})
    return render(request, 'CWBDataApp/AddColour.html')

###########################################################Add Colour
def RemoveColour(request):

    if request.method == 'POST':
        form = request.POST

        try:
            colour = Colour.objects.get(pk=form['colour'])
            colour.delete()
            return render(request, 'CWBDataApp/AddColour.html', {'dataAcceptedMessage':"Colour Successfully Deleted"})
        except:
            return render(request, 'CWBDataApp/AddColour.html', {'error_message':"Colour could not be removed because it does not exist"})
    return render(request, 'CWBDataApp/AddColour.html')

###########################################################Add Supplier
def AddSupplier(request):

    if request.method == 'POST':
        form = request.POST

        try:
            supplier = Materialcost.objects.get(pk=form['supplier'])
            return render(request, 'CWBDataApp/AddSupplier.html', {'error_message':"Supplier already exists"})
        except:
            new_supplier = Materialcost(supplier=form['supplier'],
                                        costperpound=form['price']
                                       )
            new_supplier.save()
            return render(request, 'CWBDataApp/AddSupplier.html', {'dataAcceptedMessage':"Supplier Successfully Added"})

    return render(request, 'CWBDataApp/AddSupplier.html')

###########################################################Remove Supplier
def RemoveSupplier(request):

    if request.method == 'POST':
        form = request.POST

        try:
            supplier = Materialcost.objects.get(pk=form['supplier'])
            supplier.delete()
            return render(request, 'CWBDataApp/AddSupplier.html', {'dataAcceptedMessage':"Supplier Successfully Removed"})
        except:
            return render(request, 'CWBDataApp/AddSupplier.html', {'error_message':"Supplier Cannot Be Removed Because It Does Not Exist"})
    return render(request, 'CWBDataApp/AddSupplier.html')

###########################################################Update Supplier
def UpdateSupplier(request):
    return render(request, 'CWBDataApp/UpdateSupplier.html')

###########################################################ADD PROFILE AVERAGE
def AddProfileAverage(request):

    if request.method == 'POST':
        form = request.POST

        try:
            profile = Profileaverages.objects.get(pk=form['profile'])
            return render(request, 'CWBDataApp/AddProfileAverage.html', {'error_message':"Profile already exists. If you wish to update this profile use, the UpdateProfileAverage tab under help"})
        except:
            new_average = Profileaverages(productname=form['profile'],
                                          averageskidsperday=form['average']
                                       )
            new_average.save()
            return render(request, 'CWBDataApp/AddProfileAverage.html', {'dataAcceptedMessage':"Profile Average Successfully Added"})


    return render(request, 'CWBDataApp/AddProfileAverage.html')

###########################################################UPDATE PROFILE AVERAGE
def UpdateProfileAverage(request):
    allAverages= Profileaverages.objects.all()

    if request.method == 'POST':
        form = request.POST

        try:
            profile = Profileaverages.objects.get(pk=form['profile'])
            profile.averageskidsperday = form['average']
            profile.save()
            return render(request, 'CWBDataApp/UpdateProfileAverage.html', {'allAverages':allAverages, 'dataAcceptedMessage':"Profile Average Successfully Updated"})
        except:
            return render(request, 'CWBDataApp/UpdateProfileAverage.html', {'allAverages':allAverages, 'error_message':"Profile could not be updated"})

    return render(request, 'CWBDataApp/UpdateProfileAverage.html', {'allAverages':allAverages})


###########################################################ADMIN
def admin(request):
    return reverse('admin:index')


#Add a given number of business days to a date, we ignore weekends
def addDate(startDate, numDays):
    currentDate = startDate

    while numDays > 0:
        currentDate += timedelta(days=1)
        weekday=currentDate.weekday()
        if weekday >= 5:
            continue
        else:
            numDays -= 1
    return currentDate
