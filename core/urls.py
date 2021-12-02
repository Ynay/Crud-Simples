from django.contrib import admin
from django.urls import path
from .views import ClienteList, ClienteCreate, ClienteUpdate, ClienteDetail, ClienteDelete

app_name = 'core'

urlpatterns = [
    path('', ClienteList.as_view(), name='list'),
    path('create/', ClienteCreate.as_view(), name='create'),
    path('update/<int:pk>/', ClienteUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', ClienteDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', ClienteDelete.as_view(), name='delete'),
   
]