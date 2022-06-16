from django.contrib import admin
from .models import Batchcost, Materialcost, Materialinventory, Materialtesting, Ordersheetmachine1, Ordersheetmachine2, Ordersheetmachine3,  Productinventory, Productprofiles, Colour, Profileaverages, picsum, cisEmailSubject

#Register DB tables here to be able to access them in admin mode
admin.site.register(Batchcost)
admin.site.register(Materialcost)
admin.site.register(Materialinventory)
admin.site.register(Materialtesting)
admin.site.register(Ordersheetmachine1)
admin.site.register(Ordersheetmachine2)
admin.site.register(Ordersheetmachine3)
admin.site.register(Productinventory)
admin.site.register(Productprofiles)
admin.site.register(Colour)
admin.site.register(Profileaverages)
admin.site.register(picsum)
admin.site.register(cisEmailSubject)
