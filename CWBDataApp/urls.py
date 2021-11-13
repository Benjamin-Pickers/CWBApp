from django.urls import path
from . import views

app_name = 'CWBDataApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('BatchCostTracking/', views.BatchCostTracking, name='BatchCost'),
    path('MaterialTesting/', views.MaterialTesting, name='MaterialTest'),
]
