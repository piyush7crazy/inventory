from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields=['product' , 'stock_quantities' , 'purchases' , 'sales' , 'date_time' , 'id']
