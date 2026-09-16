from rest_framework.decorators  import api_view
from rest_framework.response import Response
from .models import Inventory
from .serializers import InventorySerializer

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