from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.db import connection
import pandas as pd
import os
from datetime import date
from decimal import Decimal

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
        prod_object = Productprofiles.objects.get(pk=form['prodName'])

        if Productinventory.objects.filter(productname=prod_object, colour=form['colour']).exists():
            prod_object = Productinventory.objects.get(productname=prod_object, colour=form['colour'])
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
        prod_object =  Productprofiles.objects.get(pk=form['prodName'])

        if Productinventory.objects.filter(productname=prod_object, colour=form['colour']).exists():
            prod = Productinventory.objects.get(productname=prod_object, colour=form['colour'])
            return render(request, 'CWBDataApp/ProductInventoryQuery.html', {'allProfiles':allProfiles, 'allColours':allColours, 'product':prod, 'profile':prod_object})
        else:
            return render(request, 'CWBDataApp/ProductInventoryQuery.html', {'allProfiles':allProfiles, 'allColours':allColours, 'error_message':"This product currently does not exist in inventory. If you wish to enter its data, press the link above"})
    return render(request, 'CWBDataApp/ProductInventoryQuery.html', {'allProfiles':allProfiles, 'allColours':allColours})

###########################################################PRODUCT INVENTORY SHIPPED
def ProductInventoryShipped(request):

    allProfiles= Productprofiles.objects.all()
    allColours = Colour.objects.all()

    if request.method == 'POST':
        form = request.POST
        prod_object =  Productprofiles.objects.get(pk=form['prodName'])

        if Productinventory.objects.filter(productname=prod_object, colour=form['colour']).exists():
            prod = Productinventory.objects.get(productname=prod_object, colour=form['colour'])

            SkidsRemaining = prod.numberofskids - int(form['numSkids'])

            if SkidsRemaining <= 0:
                prod.delete()
                SkidsRemaining = 0
            else:
                prod.numberofskids = SkidsRemaining
                prod.save()
            return render(request, 'CWBDataApp/ProductInventoryShipped.html', {'allProfiles':allProfiles, 'allColours':allColours, 'dataAcceptedMessage':"Number of Skids Successfully Updated", 'skids':str(SkidsRemaining)})
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
    return render(request, 'CWBDataApp/OrderSheetsMachine1.html')

###########################################################ORDER SHEET MACHINE 2
def OrderSheetsMachine2(request):
    return render(request, 'CWBDataApp/OrderSheetsMachine2.html')

###########################################################ORDER SHEET MACHINE 3
def OrderSheetsMachine3(request):
    return render(request, 'CWBDataApp/OrderSheetsMachine3.html')

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


###########################################################ADMIN
def admin(request):
    return reverse('admin:index')
