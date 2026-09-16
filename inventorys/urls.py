from django.urls import path
from . import views

urlpatterns=[
    path('api/create_inventory/',views.create_inventory_api,name="create_inventory_api"),
    path('api/list_inventory/',views.list_inventory_api,name="list_inventory_api"),
    path('api/detail_inventory/<int:id>/',views.detail_inventory_api,name="detail_inventory_api"),
    path('api/update_inventory/<int:id>/',views.update_inventory_api,name="update_inventory_api"),
    path('api/delete_inventory/<int:id>/',views.delete_inventory_api,name="delete_inventory_api"),
]