from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Items
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    
    api_urls={
        'Get Items' : '/items-retrieve',
        'Get Single Item' : '/items-retrieve/<int:pk>',
        'Delete Item' : '/items-delete/<int:pk>',
        'Post Item' : '/items-post',
        'Update Items' : '/items-update/<int:pk>',
    }

    return Response(api_urls)

@api_view(['GET'])
def retrieve_items(request):
    items = Items.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def retrieve_item(request, pk):
    item = Items.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, many=False)

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_item(request, pk):
    item = Items.objects.get(id=pk)
    item.delete()

    return Response('Item deleted')

@api_view(['POST'])
def post_item(request):
    serializer=ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_item(request, pk):
    item = Items.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

