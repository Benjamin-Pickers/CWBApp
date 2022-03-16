from django.db import models
from django.forms import ModelForm
import datetime


class Batchcost(models.Model):
    batchname = models.CharField(db_column='BatchName', primary_key=True, max_length=15)  # Field name made lowercase.
    batchdate = models.DateField(db_column='BatchDate', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=10, decimal_places=2)  # Field name made lowercase.
    totalweight = models.SmallIntegerField(db_column='TotalWeight')  # Field name made lowercase.
    priceperpound = models.DecimalField(db_column='PricePerPound', max_digits=10, decimal_places=2)  # Field name made lowercase.
    material1 = models.CharField(db_column='Material1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weight1 = models.SmallIntegerField(db_column='Weight1', blank=True, null=True)  # Field name made lowercase.
    value1 = models.DecimalField(db_column='Value1', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    material2 = models.CharField(db_column='Material2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weight2 = models.SmallIntegerField(db_column='Weight2', blank=True, null=True)  # Field name made lowercase.
    value2 = models.DecimalField(db_column='Value2', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    material3 = models.CharField(db_column='Material3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weight3 = models.SmallIntegerField(db_column='Weight3', blank=True, null=True)  # Field name made lowercase.
    value3 = models.DecimalField(db_column='Value3', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    material4 = models.CharField(db_column='Material4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weight4 = models.SmallIntegerField(db_column='Weight4', blank=True, null=True)  # Field name made lowercase.
    value4 = models.DecimalField(db_column='Value4', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    material5 = models.CharField(db_column='Material5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weight5 = models.SmallIntegerField(db_column='Weight5', blank=True, null=True)  # Field name made lowercase.
    value5 = models.DecimalField(db_column='Value5', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    material6 = models.CharField(db_column='Material6', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weight6 = models.SmallIntegerField(db_column='Weight6', blank=True, null=True)  # Field name made lowercase.
    value6 = models.DecimalField(db_column='Value6', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    material7 = models.CharField(db_column='Material7', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weight7 = models.SmallIntegerField(db_column='Weight7', blank=True, null=True)  # Field name made lowercase.
    value7 = models.DecimalField(db_column='Value7', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    material8 = models.CharField(db_column='Material8', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weight8 = models.SmallIntegerField(db_column='Weight8', blank=True, null=True)  # Field name made lowercase.
    value8 = models.DecimalField(db_column='Value8', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    material9 = models.CharField(db_column='Material9', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weight9 = models.SmallIntegerField(db_column='Weight9', blank=True, null=True)  # Field name made lowercase.
    value9 = models.DecimalField(db_column='Value9', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    material10 = models.CharField(db_column='Material10', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weight10 = models.SmallIntegerField(db_column='Weight10', blank=True, null=True)  # Field name made lowercase.
    value10 = models.DecimalField(db_column='Value10', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=20, blank=True, null=True)  # Field name made lowercase.
    colourweight = models.DecimalField(db_column='ColourWeight', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    colourvalue = models.DecimalField(db_column='ColourValue', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    foamweight = models.DecimalField(db_column='FoamWeight', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    foamvalue = models.DecimalField(db_column='FoamValue', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalshredweight = models.SmallIntegerField(db_column='TotalShredWeight', blank=True, null=True)  # Field name made lowercase.
    profile = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BatchCost'


class Materialcost(models.Model):
    supplier = models.CharField(db_column='Supplier', primary_key=True, max_length=30)
    costperpound = models.DecimalField(db_column='CostPerPound', decimal_places=2, max_digits=10)

    class Meta:
        managed = False
        db_table = 'MaterialCost'


class Materialinventory(models.Model):
    materialname = models.CharField(db_column='MaterialName', primary_key=True, max_length=30)
    supplier = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier')
    numberofboxes = models.DecimalField(db_column='NumberofBoxes', max_digits=10, decimal_places=1)
    locations = models.CharField(db_column='Locations', max_length=20, blank=True, null=True)
    premixed = models.BooleanField(db_column='PreMixed')
    priceperpound = models.DecimalField(db_column='PricePerPound', decimal_places=2, max_digits=10)

    class Meta:
        managed = False
        db_table = 'MaterialInventory'


class Materialtesting(models.Model):
    projectnumber = models.SmallIntegerField(db_column='ProjectNumber')  # Field name made lowercase.
    testname = models.ForeignKey(Batchcost, models.DO_NOTHING, db_column='TestName')  # Field name made lowercase.
    testnumber = models.SmallIntegerField(db_column='TestNumber')  # Field name made lowercase.
    testdate = models.DateField(db_column='TestDate', blank=True, null=True)  # Field name made lowercase.
    labourused = models.CharField(db_column='LabourUsed', max_length=50)  # Field name made lowercase.
    machinetimeused = models.DecimalField(db_column='MachineTimeUsed', max_digits=3, decimal_places=1)  # Field name made lowercase.
    productionline = models.SmallIntegerField(db_column='ProductionLine', blank=True, null=True)  # Field name made lowercase.
    materialstested = models.CharField(db_column='MaterialsTested', max_length=200)  # Field name made lowercase.
    othermaterialstested = models.CharField(db_column='OtherMaterialsTested', max_length=200, blank=True, null=True)  # Field name made lowercase.
    moulds = models.CharField(db_column='Moulds', max_length=40)  # Field name made lowercase.
    reasonfortest = models.CharField(db_column='ReasonForTest', max_length=200, blank=True, null=True)  # Field name made lowercase.
    expectedresults = models.CharField(db_column='ExpectedResults', max_length=200, blank=True, null=True)  # Field name made lowercase.
    difficultiesencountered = models.CharField(db_column='DifficultiesEncountered', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nextstep = models.CharField(db_column='NextStep', max_length=100)  # Field name made lowercase.
    estimatedcostofmaterial = models.SmallIntegerField(db_column='EstimatedCostofMaterial')  # Field name made lowercase.
    estimatedcostoflabour = models.SmallIntegerField(db_column='EstimatedCostofLabour')  # Field name made lowercase.
    totalcostoftest = models.SmallIntegerField(db_column='TotalCostofTest')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaterialTesting'


class Mixingform(models.Model):
    batchname = models.CharField(db_column='BatchName', primary_key=True, max_length=15)  # Field name made lowercase.
    batchdate = models.DateField(db_column='BatchDate', blank=True, null=True)  # Field name made lowercase.
    material1 = models.CharField(db_column='Material1', max_length=20)  # Field name made lowercase.
    weight1 = models.SmallIntegerField(db_column='Weight1', blank=True, null=True)  # Field name made lowercase.
    supplier1 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier1', related_name='rawsupplier1', blank=True, null=True)  # Field name made lowercase.
    material2 = models.CharField(db_column='Material2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight2 = models.SmallIntegerField(db_column='Weight2', blank=True, null=True)  # Field name made lowercase.
    supplier2 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier2', related_name='rawsupplier2', blank=True, null=True)  # Field name made lowercase.
    material3 = models.CharField(db_column='Material3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight3 = models.SmallIntegerField(db_column='Weight3', blank=True, null=True)  # Field name made lowercase.
    supplier3 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier3', related_name='rawsupplier3', blank=True, null=True)  # Field name made lowercase.
    material4 = models.CharField(db_column='Material4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight4 = models.SmallIntegerField(db_column='Weight4', blank=True, null=True)  # Field name made lowercase.
    supplier4 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier4', related_name='rawsupplier4', blank=True, null=True)  # Field name made lowercase.
    material5 = models.CharField(db_column='Material5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight5 = models.SmallIntegerField(db_column='Weight5', blank=True, null=True)  # Field name made lowercase.
    supplier5 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier5', related_name='rawsupplier5', blank=True, null=True)  # Field name made lowercase.
    material6 = models.CharField(db_column='Material6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight6 = models.SmallIntegerField(db_column='Weight6', blank=True, null=True)  # Field name made lowercase.
    supplier6 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier6', related_name='rawsupplier6', blank=True, null=True)  # Field name made lowercase.
    material7 = models.CharField(db_column='Material7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight7 = models.SmallIntegerField(db_column='Weight7', blank=True, null=True)  # Field name made lowercase.
    supplier7 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier7', related_name='rawsupplier7', blank=True, null=True)  # Field name made lowercase.
    material8 = models.CharField(db_column='Material8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight8 = models.SmallIntegerField(db_column='Weight8', blank=True, null=True)  # Field name made lowercase.
    supplier8 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier8', related_name='rawsupplier8', blank=True, null=True)  # Field name made lowercase.
    material9 = models.CharField(db_column='Material9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight9 = models.SmallIntegerField(db_column='Weight9', blank=True, null=True)  # Field name made lowercase.
    supplier9 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier9', related_name='rawsupplier9', blank=True, null=True)  # Field name made lowercase.
    material10 = models.CharField(db_column='Material10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight10 = models.SmallIntegerField(db_column='Weight10', blank=True, null=True)  # Field name made lowercase.
    supplier10 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier10', related_name='rawsupplier10', blank=True, null=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=20, blank=True, null=True)  # Field name made lowercase.
    colourweight = models.FloatField(db_column='ColourWeight', blank=True, null=True)  # Field name made lowercase.
    foamweight = models.FloatField(db_column='FoamWeight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MixingForm'

class Ordersheetmachine1(models.Model):
    ponumber = models.AutoField(db_column='PONumber', primary_key=True)  # Field name made lowercase.
    customerponumber = models.CharField(db_column='CustomerPONumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    projectedstartdate = models.DateField(db_column='ProjectedStartDate')  # Field name made lowercase.
    projectedenddate = models.DateField(db_column='ProjectedEndDate')  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate')  # Field name made lowercase.
    lengthofrunindays = models.DecimalField(db_column='LengthofRuninDays', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    priorityrank = models.SmallIntegerField(db_column='PriorityRank')  # Field name made lowercase.
    boardprofile = models.CharField(db_column='BoardProfile', max_length=40)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=15)  # Field name made lowercase.
    skidsremaining = models.DecimalField(db_column='SkidsRemaining', max_digits=6, decimal_places=2)  # Field name made lowercase.
    pcs = models.SmallIntegerField(db_column='PCS')  # Field name made lowercase.
    pcssent = models.SmallIntegerField(db_column='PCSSent', blank=True, null=True)  # Field name made lowercase.
    pcsremaining = models.SmallIntegerField(db_column='PCSRemaining')  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qualitynotes = models.CharField(db_column='QualityNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pcsinventorized = models.SmallIntegerField(db_column='PcsInventorized', blank=True, null=True)  # Field name made lowercase

    class Meta:
        managed = False
        db_table = 'OrderSheetMachine1'


class Ordersheetmachine2(models.Model):
    ponumber = models.AutoField(db_column='PONumber', primary_key=True)  # Field name made lowercase.
    customerponumber = models.CharField(db_column='CustomerPONumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    projectedstartdate = models.DateField(db_column='ProjectedStartDate')  # Field name made lowercase.
    projectedenddate = models.DateField(db_column='ProjectedEndDate')  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate')  # Field name made lowercase.
    lengthofrunindays = models.DecimalField(db_column='LengthofRuninDays', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    priorityrank = models.SmallIntegerField(db_column='PriorityRank')  # Field name made lowercase.
    boardprofile = models.CharField(db_column='BoardProfile', max_length=40)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=15)  # Field name made lowercase.
    skidsremaining = models.DecimalField(db_column='SkidsRemaining', max_digits=6, decimal_places=2)  # Field name made lowercase.
    pcs = models.SmallIntegerField(db_column='PCS')  # Field name made lowercase.
    pcssent = models.SmallIntegerField(db_column='PCSSent', blank=True, null=True)  # Field name made lowercase.
    pcsremaining = models.SmallIntegerField(db_column='PCSRemaining')  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qualitynotes = models.CharField(db_column='QualityNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pcsinventorized = models.SmallIntegerField(db_column='PcsInventorized', blank=True, null=True)  # Field name made lowercase

    class Meta:
        managed = False
        db_table = 'OrderSheetMachine2'


class Ordersheetmachine3(models.Model):
    ponumber = models.AutoField(db_column='PONumber', primary_key=True)  # Field name made lowercase.
    customerponumber = models.CharField(db_column='CustomerPONumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    projectedstartdate = models.DateField(db_column='ProjectedStartDate')  # Field name made lowercase.
    projectedenddate = models.DateField(db_column='ProjectedEndDate')  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate')  # Field name made lowercase.
    lengthofrunindays = models.DecimalField(db_column='LengthofRuninDays', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    priorityrank = models.SmallIntegerField(db_column='PriorityRank')  # Field name made lowercase.
    boardprofile = models.CharField(db_column='BoardProfile', max_length=40)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=15)  # Field name made lowercase.
    skidsremaining = models.DecimalField(db_column='SkidsRemaining', max_digits=6, decimal_places=2)  # Field name made lowercase.
    pcs = models.SmallIntegerField(db_column='PCS')  # Field name made lowercase.
    pcssent = models.SmallIntegerField(db_column='PCSSent', blank=True, null=True)  # Field name made lowercase.
    pcsremaining = models.SmallIntegerField(db_column='PCSRemaining')  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qualitynotes = models.CharField(db_column='QualityNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pcsinventorized = models.SmallIntegerField(db_column='PcsInventorized', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderSheetMachine3'


class Productinventory(models.Model):
    productname = models.CharField(db_column='ProductName', max_length=40)
    colour = models.CharField(db_column='colour', max_length=15)
    embossed = models.BooleanField(db_column='Embossed')
    doublesided = models.BooleanField(db_column='DoubleSided')
    numberofskids = models.DecimalField(db_column='NumberOfSkids', max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ProductInventory'

class Productprofiles(models.Model):
    productname = models.CharField(db_column='ProductName', primary_key=True, max_length=40)
    pcsperskid = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProductProfiles'

class Colour(models.Model):
    colour = models.CharField(max_length=15, primary_key=True)
    priceperpound = models.DecimalField(max_digits=5, decimal_places=2, null=True)

class Employees(models.Model):
    employeename = models.CharField(db_column='EmployeeName', primary_key=True, max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employees'

class Profileaverages(models.Model):
    productname = models.CharField(db_column='ProductName', primary_key=True, max_length=40)  # Field name made lowercase.
    averageskidsperday = models.DecimalField(db_column='AverageSkidsPerDay', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProfileAverages'

class picsum(models.Model):
    title = models.CharField(max_length=40, primary_key=True, default="Test")
    testdate = models.DateField(default=datetime.date.today)
    supervisor = models.CharField(max_length=40, null=True)
    machineoperator = models.CharField(max_length=40, null=True)
    temp1 = models.BooleanField()
    mixer = models.CharField(max_length=40, null=True)
    temp2 = models.BooleanField()
    image = models.ImageField(upload_to="PicAndSum/%Y/%m", blank=True)
    description = models.TextField(null=True)

class picsumForm(ModelForm):
    class Meta:
        model = picsum
        fields = ['title', 'testdate', 'machineoperator', 'temp1', 'mixer', 'temp2', 'image', 'description']
