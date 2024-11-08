from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import status
from  django.shortcuts import get_object_or_404

# Quick Starter for DRF - All Items
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

# Quick Starter for DRF - Single Item
# class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer


@api_view(['GET','POST'])
def menu_items(request):
    if request.method=='GET':
        items = MenuItem.objects.select_related('category').all() # Select related data in single SQL Call
        serialized_item = MenuItemSerializer(items,many=True) # Serialize
        return Response(serialized_item.data)
    if request.method =='POST':
        deserialized_item = MenuItemSerializer(data=request.data) # DeSerialize 
        deserialized_item.is_valid(raise_exception=True) # validate data
        deserialized_item.save() # Saves data to db
        return Response(deserialized_item.data, status.HTTP_201_CREATED) # Access data after saving
        

@api_view(['GET','POST'])
def single_item(request,id):
    item = get_object_or_404(MenuItem,pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)