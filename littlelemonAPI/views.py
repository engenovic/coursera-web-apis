from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from  django.shortcuts import get_object_or_404

# Quick Starter for DRF - All Items
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

# Quick Starter for DRF - Single Item
# class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer


@api_view()
def menu_items(request):
    items = MenuItem.objects.select_related('category').all() # Select related data in single SQL Call
    serialized_item = MenuItemSerializer(items,many=True)
    return Response(serialized_item.data)

@api_view()
def single_item(request,id):
    item = get_object_or_404(MenuItem,pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)