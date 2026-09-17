from rest_framework import serializers
from .models import Inventory , Purchase , Sales

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields=['product' , 'stock_quantities' , 'id']


class PurchaseSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product' , read_only=True)
    class Meta:
        model=Purchase
        fields=['product' , 'amount' , 'date_time' , 'product_name' , 'id']


class SalesSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product', read_only=True)
    class Meta:
        model=Sales
        fields=['product' , 'amount' , 'date_time' , 'product_name' , 'id']
        