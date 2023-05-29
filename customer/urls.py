from django.urls import path
from . import views

urlpatterns = [
    path('customer/create/', views.create_customer, name='create_customer'),
    path('customer/', views.customer_list, name='customer_list'),
    path('customer/update/<str:id_cust>/', views.update_customer, name='update_customer'),
    path('customer/delete/<str:id_cust>/', views.delete_customer, name='delete_customer'),
]
