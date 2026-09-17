from django.urls import path
from . import views

urlpatterns=[
    path('api/create_inventory/',views.create_inventory_api,name="create_inventory_api"),
    path('api/list_inventory/',views.list_inventory_api,name="list_inventory_api"),
    path('api/detail_inventory/<int:id>/',views.detail_inventory_api,name="detail_inventory_api"),
    path('api/update_inventory/<int:id>/',views.update_inventory_api,name="update_inventory_api"),
    path('api/delete_inventory/<int:id>/',views.delete_inventory_api,name="delete_inventory_api"),


    path('api/create_purchase/',views.create_purchase_api,name="create_purchase_api"),
    path('api/list_purchase/',views.list_purchase_api,name="list_purchase_api"),
    path('api/detail_purchase/<int:id>/',views.detail_purchase_api,name="detail_purchase_api"),
    path('api/update_purchase/<int:id>/',views.update_purchase_api,name="update_purchase_api"),
    path('api/delete_purchase/<int:id>/',views.delete_purchase_api,name="delete_purchase_api"),


    path('api/create_sales/',views.create_sales_api,name="create_sales_api"),
    path('api/list_sales/',views.list_sales_api,name="list_sales_api"),
    path('api/detail_sales/<int:id>/',views.detail_sales_api,name="detail_sales_api"),
    path('api/update_sales/<int:id>/',views.update_sales_api,name="update_sales_api"),
    path('api/delete_sales/<int:id>/',views.delete_sales_api,name="delete_sales_api"),
]