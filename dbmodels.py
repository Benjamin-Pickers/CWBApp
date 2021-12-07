# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Batchcosttracking(models.Model):
    batchname = models.CharField(db_column='BatchName', primary_key=True, max_length=15)  # Field name made lowercase.
    batchdate = models.DateField(db_column='BatchDate', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=10, decimal_places=2)  # Field name made lowercase.
    totalweight = models.SmallIntegerField(db_column='TotalWeight')  # Field name made lowercase.
    priceperpound = models.DecimalField(db_column='PricePerPound', max_digits=10, decimal_places=2)  # Field name made lowercase.
    supplier1 = models.ForeignKey('Materialcost', models.DO_NOTHING, db_column='Supplier1')  # Field name made lowercase.
    weight1 = models.SmallIntegerField(db_column='Weight1', blank=True, null=True)  # Field name made lowercase.
    value1 = models.DecimalField(db_column='Value1', max_digits=10, decimal_places=3)  # Field name made lowercase.
    supplier2 = models.ForeignKey('Materialcost', models.DO_NOTHING, db_column='Supplier2', blank=True, null=True)  # Field name made lowercase.
    weight2 = models.SmallIntegerField(db_column='Weight2', blank=True, null=True)  # Field name made lowercase.
    value2 = models.DecimalField(db_column='Value2', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    supplier3 = models.ForeignKey('Materialcost', models.DO_NOTHING, db_column='Supplier3', blank=True, null=True)  # Field name made lowercase.
    weight3 = models.SmallIntegerField(db_column='Weight3', blank=True, null=True)  # Field name made lowercase.
    value3 = models.DecimalField(db_column='Value3', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    supplier4 = models.ForeignKey('Materialcost', models.DO_NOTHING, db_column='Supplier4', blank=True, null=True)  # Field name made lowercase.
    weight4 = models.SmallIntegerField(db_column='Weight4', blank=True, null=True)  # Field name made lowercase.
    value4 = models.DecimalField(db_column='Value4', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=20, blank=True, null=True)  # Field name made lowercase.
    colourweight = models.DecimalField(db_column='ColourWeight', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    colourvalue = models.DecimalField(db_column='ColourValue', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    foam = models.CharField(db_column='Foam', max_length=4, blank=True, null=True)  # Field name made lowercase.
    foamweight = models.DecimalField(db_column='FoamWeight', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    foamvalue = models.DecimalField(db_column='FoamValue', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    totalshredweight = models.SmallIntegerField(db_column='TotalShredWeight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BatchCostTracking'


class CwbdataappColour(models.Model):
    colour = models.CharField(primary_key=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'CWBDataApp_colour'


class Employees(models.Model):
    employeename = models.CharField(db_column='EmployeeName', primary_key=True, max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employees'


class Materialcost(models.Model):
    supplier = models.CharField(db_column='Supplier', primary_key=True, max_length=30)  # Field name made lowercase.
    costperpound = models.DecimalField(db_column='CostPerPound', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaterialCost'


class Materialinventory(models.Model):
    materialname = models.CharField(db_column='MaterialName', primary_key=True, max_length=30)  # Field name made lowercase.
    supplier = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier')  # Field name made lowercase.
    numberofboxes = models.DecimalField(db_column='NumberofBoxes', max_digits=10, decimal_places=1)  # Field name made lowercase.
    locations = models.CharField(db_column='Locations', max_length=20, blank=True, null=True)  # Field name made lowercase.
    premixed = models.BooleanField(db_column='PreMixed')  # Field name made lowercase.
    priceperpound = models.DecimalField(db_column='PricePerPound', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

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
    supplier1 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier1', blank=True, null=True)  # Field name made lowercase.
    material2 = models.CharField(db_column='Material2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight2 = models.SmallIntegerField(db_column='Weight2', blank=True, null=True)  # Field name made lowercase.
    supplier2 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier2', blank=True, null=True)  # Field name made lowercase.
    material3 = models.CharField(db_column='Material3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight3 = models.SmallIntegerField(db_column='Weight3', blank=True, null=True)  # Field name made lowercase.
    supplier3 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier3', blank=True, null=True)  # Field name made lowercase.
    material4 = models.CharField(db_column='Material4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight4 = models.SmallIntegerField(db_column='Weight4', blank=True, null=True)  # Field name made lowercase.
    supplier4 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier4', blank=True, null=True)  # Field name made lowercase.
    material5 = models.CharField(db_column='Material5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight5 = models.SmallIntegerField(db_column='Weight5', blank=True, null=True)  # Field name made lowercase.
    supplier5 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier5', blank=True, null=True)  # Field name made lowercase.
    material6 = models.CharField(db_column='Material6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight6 = models.SmallIntegerField(db_column='Weight6', blank=True, null=True)  # Field name made lowercase.
    supplier6 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier6', blank=True, null=True)  # Field name made lowercase.
    material7 = models.CharField(db_column='Material7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight7 = models.SmallIntegerField(db_column='Weight7', blank=True, null=True)  # Field name made lowercase.
    supplier7 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier7', blank=True, null=True)  # Field name made lowercase.
    material8 = models.CharField(db_column='Material8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight8 = models.SmallIntegerField(db_column='Weight8', blank=True, null=True)  # Field name made lowercase.
    supplier8 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier8', blank=True, null=True)  # Field name made lowercase.
    material9 = models.CharField(db_column='Material9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight9 = models.SmallIntegerField(db_column='Weight9', blank=True, null=True)  # Field name made lowercase.
    supplier9 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier9', blank=True, null=True)  # Field name made lowercase.
    material10 = models.CharField(db_column='Material10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight10 = models.SmallIntegerField(db_column='Weight10', blank=True, null=True)  # Field name made lowercase.
    supplier10 = models.ForeignKey(Materialcost, models.DO_NOTHING, db_column='Supplier10', blank=True, null=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=20, blank=True, null=True)  # Field name made lowercase.
    colourweight = models.FloatField(db_column='ColourWeight', blank=True, null=True)  # Field name made lowercase.
    foamweight = models.FloatField(db_column='FoamWeight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MixingForm'


class Ordersheetmachine1(models.Model):
    ponumber = models.CharField(db_column='PONumber', primary_key=True, max_length=15)  # Field name made lowercase.
    projectedstartdate = models.DateField(db_column='ProjectedStartDate')  # Field name made lowercase.
    projectedenddate = models.DateField(db_column='ProjectedEndDate')  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate')  # Field name made lowercase.
    lengthofrunindays = models.DecimalField(db_column='LengthofRuninDays', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    priorityrank = models.SmallIntegerField(db_column='PriorityRank')  # Field name made lowercase.
    boardprofile = models.CharField(db_column='BoardProfile', max_length=40)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=15)  # Field name made lowercase.
    skidsremaining = models.FloatField(db_column='SkidsRemaining')  # Field name made lowercase.
    pcs = models.SmallIntegerField(db_column='PCS')  # Field name made lowercase.
    pcssent = models.SmallIntegerField(db_column='PCSSent')  # Field name made lowercase.
    pcsremaining = models.SmallIntegerField(db_column='PCSRemaining')  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=20)  # Field name made lowercase.
    qualitynotes = models.CharField(db_column='QualityNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderSheetMachine1'
        unique_together = (('ponumber', 'boardprofile', 'colour', 'duedate'),)


class Ordersheetmachine2(models.Model):
    ponumber = models.CharField(db_column='PONumber', primary_key=True, max_length=15)  # Field name made lowercase.
    projectedstartdate = models.DateField(db_column='ProjectedStartDate')  # Field name made lowercase.
    projectedenddate = models.DateField(db_column='ProjectedEndDate')  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate')  # Field name made lowercase.
    lengthofrunindays = models.DecimalField(db_column='LengthofRuninDays', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    priorityrank = models.SmallIntegerField(db_column='PriorityRank')  # Field name made lowercase.
    boardprofile = models.CharField(db_column='BoardProfile', max_length=40)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=15)  # Field name made lowercase.
    skidsremaining = models.FloatField(db_column='SkidsRemaining')  # Field name made lowercase.
    pcs = models.SmallIntegerField(db_column='PCS')  # Field name made lowercase.
    pcssent = models.SmallIntegerField(db_column='PCSSent')  # Field name made lowercase.
    pcsremaining = models.SmallIntegerField(db_column='PCSRemaining')  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=20)  # Field name made lowercase.
    qualitynotes = models.CharField(db_column='QualityNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderSheetMachine2'
        unique_together = (('ponumber', 'boardprofile', 'colour', 'duedate'),)


class Ordersheetmachine3(models.Model):
    ponumber = models.CharField(db_column='PONumber', primary_key=True, max_length=15)  # Field name made lowercase.
    projectedstartdate = models.DateField(db_column='ProjectedStartDate')  # Field name made lowercase.
    projectedenddate = models.DateField(db_column='ProjectedEndDate')  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate')  # Field name made lowercase.
    lengthofrunindays = models.DecimalField(db_column='LengthofRuninDays', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    priorityrank = models.SmallIntegerField(db_column='PriorityRank')  # Field name made lowercase.
    boardprofile = models.CharField(db_column='BoardProfile', max_length=40)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=15)  # Field name made lowercase.
    skidsremaining = models.FloatField(db_column='SkidsRemaining')  # Field name made lowercase.
    pcs = models.SmallIntegerField(db_column='PCS')  # Field name made lowercase.
    pcssent = models.SmallIntegerField(db_column='PCSSent')  # Field name made lowercase.
    pcsremaining = models.SmallIntegerField(db_column='PCSRemaining')  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=20)  # Field name made lowercase.
    qualitynotes = models.CharField(db_column='QualityNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderSheetMachine3'
        unique_together = (('ponumber', 'boardprofile', 'colour', 'duedate'),)


class Picandsum(models.Model):
    startdate = models.DateField(db_column='StartDate', primary_key=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PicAndSum'


class Productinventory(models.Model):
    productname = models.CharField(db_column='ProductName', max_length=40)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=15)  # Field name made lowercase.
    embossed = models.BooleanField(db_column='Embossed')  # Field name made lowercase.
    doublesided = models.BooleanField(db_column='DoubleSided')  # Field name made lowercase.
    numberofskids = models.SmallIntegerField(db_column='NumberOfSkids')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductInventory'


class Productprofiles(models.Model):
    productname = models.CharField(db_column='ProductName', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductProfiles'


class Profileaverages(models.Model):
    productname = models.CharField(db_column='ProductName', primary_key=True, max_length=40)  # Field name made lowercase.
    averageskidsperday = models.DecimalField(db_column='AverageSkidsPerDay', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProfileAverages'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
