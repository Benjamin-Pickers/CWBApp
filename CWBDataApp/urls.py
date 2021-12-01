from django.urls import path
from . import views

app_name = 'CWBDataApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('BatchCostTracking/', views.BatchCostTracking, name='BatchCost'),
    path('BatchCostQuery/', views.BatchCostQuery, name='BatchCostQuery'),
    path('BatchCostExcel/', views.BatchCostExcel, name='BatchCostExcel'),
    path('MaterialTesting/', views.MaterialTesting, name='MaterialTest'),
    path('MaterialTestingPopulate/', views.MaterialTestingPopulate, name='MaterialTestPopulate'),
    path('MaterialTestQuery/', views.MaterialTestQuery, name='MaterialTestQuery'),
    path('ProductInventory/', views.ProductInventory, name='ProductInventory'),
    path('ProductInventoryUpdate/', views.ProductInventoryUpdate, name='ProductInventoryUpdate'),
    path('ProductInventoryUpdateSkids/', views.ProductInventoryUpdateSkids, name='ProductInventoryUpdateSkids'),
    path('ProductInventoryQuery/', views.ProductInventoryQuery, name='ProductInventoryQuery'),
    path('ProductInventoryShipped/', views.ProductInventoryShipped, name='ProductInventoryShipped'),
    path('MaterialInventory/', views.MaterialInventory, name='MaterialInventory'),
    path('MaterialInventoryQuery/', views.MaterialInventoryQuery, name='MaterialInventoryQuery'),
    path('MaterialInventoryUpdate/', views.MaterialInventoryUpdate, name='MaterialInventoryUpdate'),
    path('MaterialInventoryUpdateNumSkids/', views.MaterialInventoryUpdateNumSkids, name='MaterialInventoryUpdateNumSkids'),
    path('OrderSheetsMachine1/', views.OrderSheetsMachine1, name='OrderSheetsMachine1'),
    path('OrderSheetsMachine2/', views.OrderSheetsMachine2, name='OrderSheetsMachine2'),
    path('OrderSheetsMachine3/', views.OrderSheetsMachine3, name='OrderSheetsMachine3'),
    path('help/', views.help, name='help'),
    path('AddEmployee/', views.AddEmployee, name='AddEmployee'),
    path('AddBoardProfile/', views.AddBoardProfile, name='AddBoardProfile'),
    path('AddColour/', views.AddColour, name='AddColour'),
    path('AddSupplier/', views.AddSupplier, name='AddSupplier'),
    path('UpdateSupplier/', views.UpdateSupplier, name='UpdateSupplier'),
]
