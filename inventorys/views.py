from rest_framework.decorators  import api_view
from rest_framework.response import Response
from .models import Inventory , Purchase , Sales
from .serializers import InventorySerializer , PurchaseSerializer , SalesSerializer

@api_view(['POST'])
def create_inventory_api(request):
    serializer=InventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors , staus=400)

@api_view(['GET'])
def list_inventory_api(request):
    inv=Inventory.objects.all()
    serializer=InventorySerializer(inv , many=True)
    return Response(serializer.data , status=200)


@api_view(['GET'])
def detail_inventory_api(request,id):
    inv=Inventory.objects.get(id=id)
    serializer=InventorySerializer(inv)
    return Response(serializer.data , status=200)


@api_view(['PATCH'])
def update_inventory_api(request,id):
    inv=Inventory.objects.get(id=id)
    serializer=InventorySerializer(inv,data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=206)
    return Response(serializer.errors , status=400)


@api_view(['DELETE'])
def delete_inventory_api(request,id):
    inv=Inventory.objects.get(id=id)
    inv.delete()
    return Response(status=204)



@api_view(['POST'])
def create_purchase_api(request):
    serializer=PurchaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=201)
    return Response(serializer.errors , status=400)


@api_view(['GET'])
def list_purchase_api(request):
    p=Purchase.objects.all()
    serializer=PurchaseSerializer(p, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def detail_purchase_api(request,id):
    p=Purchase.objects.get(id=id)
    serializer=PurchaseSerializer(p)
    return Response(serializer.data , status=200)


@api_view(['PATCH'])
def update_purchase_api(request,id):
    p=Purchase.objects.get(id=id)
    serializer=PurchaseSerializer(p , data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data ,status=206)
    return Response(serializer.errors , status=400)


@api_view(['DELETE'])
def delete_purchase_api(request,id):
    p=Purchase.objects.get(id=id)
    p.delete()
    return Response(status=204)



@api_view(['POST'])
def create_sales_api(request):
    serializer=SalesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data ,  status=201)
    return Response(serializer.errors , status=400)


@api_view(['GET'])
def list_sales_api(request):
    s=Sales.objects.all()
    serializer=SalesSerializer(s , many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def detail_sales_api(request,id):
    s=Sales.objects.get(id=id)
    serializer=SalesSerializer(s)
    return Response(serializer.data , status=200)


@api_view(['PATCH'])
def update_sales_api(request,id):
    s=Sales.objects.get(id=id)
    serializer=SalesSerializer(s , data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=206)
    return Response(serializer.errors , status=400)


@api_view(['DELETE'])
def delete_sales_api(request,id):
    s=Sales.objects.get(id=id)
    s.delete()
    return Response(status=204)
