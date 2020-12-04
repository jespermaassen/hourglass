from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.index, name='api'),
    path('contracts/', views.showContracts, name='contracts'), 
    path('contract-detail/<str:pk>/', views.detailContract, name='contract-detail'), 
    path('contract-create', views.createContract, name='contract-create'),
    path('contract-update/<str:pk>/', views.updateContract, name='contract-update'),
    path('contract-delete/<str:pk>/', views.deleteContract, name='contract-delete'),

]