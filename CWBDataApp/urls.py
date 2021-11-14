from django.urls import path
from . import views

app_name = 'CWBDataApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('BatchCostTracking/', views.BatchCostTracking, name='BatchCost'),
    path('MaterialTesting/', views.MaterialTesting, name='MaterialTest'),
    path('ProductInventory/', views.ProductInventory, name='ProductInventory'),
    path('MaterialInventory/', views.MaterialInventory, name='MaterialInventory'),
    path('OrderSheets/', views.OrderSheets, name='OrderSheets'),
    path('help/', views.help, name='help'),
]
