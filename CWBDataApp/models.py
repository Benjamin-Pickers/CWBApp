from django.db import models

class Batchcosttracking(models.Model):
    batchname = models.CharField(db_column='BatchName', primary_key=True, max_length=15)
    batchdate = models.DateField(db_column='BatchDate', blank=True, null=True)
    totalcost = models.FloatField(db_column='TotalCost')
    totalweight = models.SmallIntegerField(db_column='TotalWeight')
    priceperpound = models.FloatField(db_column='PricePerPound')
    supplier1 = models.ForeignKey('Materialcost', models.DO_NOTHING, db_column='Supplier1',  related_name='supplier1')
    weight1 = models.SmallIntegerField(db_column='Weight1', blank=True, null=True)
    value1 = models.FloatField(db_column='Value1', blank=True, null=True)
    supplier2 = models.ForeignKey('Materialcost', models.DO_NOTHING, db_column='Supplier2', related_name='supplier2', blank=True, null=True)
    weight2 = models.SmallIntegerField(db_column='Weight2', blank=True, null=True)
    value2 = models.FloatField(db_column='Value2', blank=True, null=True)
    supplier3 = models.ForeignKey('Materialcost', models.DO_NOTHING, db_column='Supplier3', related_name='supplier3', blank=True, null=True)
    weight3 = models.SmallIntegerField(db_column='Weight3', blank=True, null=True)
    value3 = models.FloatField(db_column='Value3', blank=True, null=True)
    supplier4 = models.ForeignKey('Materialcost', models.DO_NOTHING, db_column='Supplier4', related_name='supplier4', blank=True, null=True)
    weight4 = models.SmallIntegerField(db_column='Weight4', blank=True, null=True)
    value4 = models.FloatField(db_column='Value4', blank=True, null=True)
    colour = models.CharField(db_column='Colour', max_length=20, blank=True, null=True)
    colourweight = models.FloatField(db_column='ColourWeight', blank=True, null=True)
    colourvalue = models.FloatField(db_column='ColourValue', blank=True, null=True)
    foam = models.CharField(db_column='Foam', max_length=4, blank=True, null=True)
    foamweight = models.FloatField(db_column='FoamWeight', blank=True, null=True)
    foamvalue = models.FloatField(db_column='FoamValue', blank=True, null=True)
    totalshredweight = models.SmallIntegerField(db_column='TotalShredWeight', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BatchCostTracking'


class Materialcost(models.Model):
    supplier = models.CharField(db_column='Supplier', primary_key=True, max_length=30)
    costperpound = models.FloatField(db_column='CostPerPound')

    class Meta:
        managed = False
        db_table = 'MaterialCost'


class Materialinventory(models.Model):
    materialname = models.CharField(db_column='MaterialName', primary_key=True, max_length=30)
    supplier = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier')
    numberofboxes = models.SmallIntegerField(db_column='NumberofBoxes')
    locations = models.CharField(db_column='Locations', max_length=20, blank=True, null=True)
    premixed = models.BooleanField(db_column='PreMixed')
    priceperpound = models.FloatField(db_column='PricePerPound')

    class Meta:
        managed = False
        db_table = 'MaterialInventory'


class Materialtesting(models.Model):
    projectnumber = models.SmallIntegerField(db_column='ProjectNumber')
    testname = models.ForeignKey(Batchcosttracking, models.DO_NOTHING, db_column='TestName', primary_key=True)
    testnumber = models.SmallIntegerField(db_column='TestNumber')
    testdate = models.DateField(db_column='TestDate', blank=True, null=True)
    labourused = models.CharField(db_column='LabourUsed', max_length=50)
    machinetimeused = models.SmallIntegerField(db_column='MachineTimeUsed')
    productionline = models.SmallIntegerField(db_column='ProductionLine', blank=True, null=True)
    materialstested = models.CharField(db_column='MaterialsTested', max_length=200)
    othermaterialstested = models.CharField(db_column='OtherMaterialsTested', max_length=200, blank=True, null=True)
    moulds = models.CharField(db_column='Moulds', max_length=40)
    reasonfortest = models.CharField(db_column='ReasonForTest', max_length=200, blank=True, null=True)
    expectedresults = models.CharField(db_column='ExpectedResults', max_length=200, blank=True, null=True)
    difficultiesencountered = models.CharField(db_column='DifficultiesEncountered', max_length=200, blank=True, null=True)
    nextstep = models.CharField(db_column='NextStep', max_length=100)
    estimatedcostofmaterial = models.SmallIntegerField(db_column='EstimatedCostofMaterial')
    estimatedcostoflabour = models.SmallIntegerField(db_column='EstimatedCostofLabour')
    totalcostoftest = models.SmallIntegerField(db_column='TotalCostofTest')

    class Meta:
        managed = False
        db_table = 'MaterialTesting'
        unique_together = (('testname', 'testnumber'),)

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
    lengthofrunindays = models.FloatField(db_column='LengthofRuninDays', blank=True, null=True)
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
    lengthofrunindays = models.FloatField(db_column='LengthofRuninDays', blank=True, null=True)
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
    lengthofrunindays = models.FloatField(db_column='LengthofRuninDays', blank=True, null=True)
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
