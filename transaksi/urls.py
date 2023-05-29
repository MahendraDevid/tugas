from django.urls import path
from . import views

urlpatterns = [
    path('transaksi/', views.transaksi_list, name='transaksi_list'),
    path('create/', views.transaksi_create, name='transaksi_create'),
    path('update/<int:pk>/', views.transaksi_update, name='transaksi_update'),
    path('delete/<int:pk>/', views.transaksi_delete, name='transaksi_delete'),
]
