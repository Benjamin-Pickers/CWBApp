from django.db import models

class Batchcosttracking(models.Model):
    batchname = models.CharField(db_column='BatchName', primary_key=True, max_length=15)
    batchdate = models.DateField(db_column='BatchDate', blank=True, null=True)
    totalcost = models.DecimalField(db_column='TotalCost', decimal_places=2, max_digits=10)
    totalweight = models.SmallIntegerField(db_column='TotalWeight')
    priceperpound = models.DecimalField(db_column='PricePerPound', decimal_places=2, max_digits=10)
    supplier1 = models.ForeignKey('Materialcost', models.DO_NOTHING, db_column='Supplier1',  related_name='supplier1')
    weight1 = models.SmallIntegerField(db_column='Weight1', blank=True, null=True)
    value1 = models.DecimalField(db_column='Value1', blank=True, null=True, decimal_places=3, max_digits=10)
    supplier2 = models.ForeignKey('Materialcost', models.DO_NOTHING, db_column='Supplier2', related_name='supplier2', blank=True, null=True)
    weight2 = models.SmallIntegerField(db_column='Weight2', blank=True, null=True)
    value2 = models.DecimalField(db_column='Value2', blank=True, null=True, decimal_places=3, max_digits=10)
    supplier3 = models.ForeignKey('Materialcost', models.DO_NOTHING, db_column='Supplier3', related_name='supplier3', blank=True, null=True)
    weight3 = models.SmallIntegerField(db_column='Weight3', blank=True, null=True)
    value3 = models.DecimalField(db_column='Value3', blank=True, null=True,  decimal_places=3, max_digits=10)
    supplier4 = models.ForeignKey('Materialcost', models.DO_NOTHING, db_column='Supplier4', related_name='supplier4', blank=True, null=True)
    weight4 = models.SmallIntegerField(db_column='Weight4', blank=True, null=True)
    value4 = models.DecimalField(db_column='Value4', blank=True, null=True,  decimal_places=3, max_digits=10)
    colour = models.CharField(db_column='Colour', max_length=20, blank=True, null=True)
    colourweight = models.DecimalField(db_column='ColourWeight', blank=True, null=True, decimal_places=2, max_digits=10)
    colourvalue = models.DecimalField(db_column='ColourValue', blank=True, null=True, decimal_places=3, max_digits=10)
    foam = models.CharField(db_column='Foam', max_length=4, blank=True, null=True)
    foamweight = models.DecimalField(db_column='FoamWeight', blank=True, null=True, decimal_places=2, max_digits=10)
    foamvalue = models.DecimalField(db_column='FoamValue', blank=True, null=True,  decimal_places=3, max_digits=10)
    totalshredweight = models.SmallIntegerField(db_column='TotalShredWeight', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BatchCostTracking'

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
    testname = models.ForeignKey(Batchcosttracking, models.DO_NOTHING, db_column='TestName')  # Field name made lowercase.
    testnumber = models.SmallIntegerField(db_column='TestNumber')  # Field name made lowercase.
    testdate = models.DateField(db_column='TestDate', blank=True, null=True)  # Field name made lowercase.
    labourused = models.CharField(db_column='LabourUsed', max_length=50)  # Field name made lowercase.
    machinetimeused = models.SmallIntegerField(db_column='MachineTimeUsed')  # Field name made lowercase.
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
    ponumber = models.CharField(db_column='PONumber', primary_key=True, max_length=15)
    projectedstartdate = models.DateField(db_column='ProjectedStartDate')
    projectedenddate = models.DateField(db_column='ProjectedEndDate')
    duedate = models.DateField(db_column='DueDate')
    lengthofrunindays = models.DecimalField(db_column='LengthofRuninDays', blank=True, null=True,  decimal_places=2, max_digits=10)
    priorityrank = models.SmallIntegerField(db_column='PriorityRank')
    boardprofile = models.ForeignKey('Productinventory', models.DO_NOTHING, db_column='BoardProfile', related_name='Machine1boardprofile')
    colour = models.CharField(db_column='Colour', max_length=15)
    skidsremaining = models.FloatField(db_column='SkidsRemaining')
    pcs = models.SmallIntegerField(db_column='PCS')
    pcssent = models.SmallIntegerField(db_column='PCSSent')
    pcsremaining = models.SmallIntegerField(db_column='PCSRemaining')
    customer = models.CharField(db_column='Customer', max_length=20)
    qualitynotes = models.CharField(db_column='QualityNotes', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrderSheetMachine1'
        unique_together = (('ponumber', 'boardprofile', 'colour', 'duedate'),)


class Ordersheetmachine2(models.Model):
    ponumber = models.CharField(db_column='PONumber', primary_key=True, max_length=15)
    projectedstartdate = models.DateField(db_column='ProjectedStartDate')
    projectedenddate = models.DateField(db_column='ProjectedEndDate')
    duedate = models.DateField(db_column='DueDate')
    lengthofrunindays = models.DecimalField(db_column='LengthofRuninDays', blank=True, null=True,  decimal_places=2, max_digits=10)
    priorityrank = models.SmallIntegerField(db_column='PriorityRank')
    boardprofile = models.ForeignKey('Productinventory', models.DO_NOTHING, db_column='BoardProfile', related_name='Machine2boardprofile')
    colour = models.CharField(db_column='Colour', max_length=15)
    skidsremaining = models.FloatField(db_column='SkidsRemaining')
    pcs = models.SmallIntegerField(db_column='PCS')
    pcssent = models.SmallIntegerField(db_column='PCSSent')
    pcsremaining = models.SmallIntegerField(db_column='PCSRemaining')
    customer = models.CharField(db_column='Customer', max_length=20)
    qualitynotes = models.CharField(db_column='QualityNotes', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrderSheetMachine2'
        unique_together = (('ponumber', 'boardprofile', 'colour', 'duedate'),)


class Ordersheetmachine3(models.Model):
    ponumber = models.CharField(db_column='PONumber', primary_key=True, max_length=15)
    projectedstartdate = models.DateField(db_column='ProjectedStartDate')
    projectedenddate = models.DateField(db_column='ProjectedEndDate')
    duedate = models.DateField(db_column='DueDate')
    lengthofrunindays = models.DecimalField(db_column='LengthofRuninDays', blank=True, null=True, decimal_places=2, max_digits=10)
    priorityrank = models.SmallIntegerField(db_column='PriorityRank')
    boardprofile = models.ForeignKey('Productinventory', models.DO_NOTHING, db_column='BoardProfile', related_name='Machine3boardprofile')
    colour = models.CharField(db_column='Colour', max_length=15)
    skidsremaining = models.FloatField(db_column='SkidsRemaining')
    pcs = models.SmallIntegerField(db_column='PCS')
    pcssent = models.SmallIntegerField(db_column='PCSSent')
    pcsremaining = models.SmallIntegerField(db_column='PCSRemaining')
    customer = models.CharField(db_column='Customer', max_length=20)
    qualitynotes = models.CharField(db_column='QualityNotes', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrderSheetMachine3'
        unique_together = (('ponumber', 'boardprofile', 'colour', 'duedate'),)


class Picandsum(models.Model):
    startdate = models.DateField(db_column='StartDate', primary_key=True)
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)
    link = models.CharField(db_column='Link', max_length=100)

    class Meta:
        managed = False
        db_table = 'PicAndSum'


class Productinventory(models.Model):
    productname = models.CharField(db_column='ProductName', max_length=40)
    colour = models.CharField(db_column='colour', max_length=15)
    embossed = models.BooleanField(db_column='Embossed')
    doublesided = models.BooleanField(db_column='DoubleSided')
    numberofskids = models.SmallIntegerField(db_column='NumberOfSkids')

    class Meta:
        managed = False
        db_table = 'ProductInventory'

class Productprofiles(models.Model):
    productname = models.CharField(db_column='ProductName', primary_key=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'ProductProfiles'

class Colour(models.Model):
    colour = models.CharField(max_length=15, primary_key=True)

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
