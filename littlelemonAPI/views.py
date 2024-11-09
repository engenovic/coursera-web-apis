from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import status
from  django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,  permission_classes, throttle_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


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
        category_name = request.query_params.get('category') #filter param Category
        to_price = request.query_params.get('to_price') #filter param Price
        search = request.query_params.get('search') #search param item title
        order = request.query_params.get('order') #order param item price
        perpage = request.query_params.get('perpage',default=2) #perpage param items per page
        page    = request.query_params.get('page',default=1) #page param page number
        if category_name:
            items = items.filter(category__slug=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        if search:
            items = items.filter(title__icontains=search)
        if order:
         items = items.order_by(order)
         
        paginator = Paginator(items,per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items= []
        serialized_item = MenuItemSerializer(items,many=True) # Serialize items
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

# @api_view()
# @permission_classes([IsAuthenticated])
# def secret(request):
#     return Response({"message":"some secret message"})

@api_view()
@permission_classes([IsAuthenticated])
def me(request):
    return Response(request.user.email)

@api_view()
@permission_classes([IsAuthenticated])
def manager(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message":"Only manager should view this"})
    else:
        return Response({"message":"You are not authorized"},403)

@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"Successful"})

@api_view()
@throttle_classes([UserRateThrottle])
def throttle_check_auth(request):
    return Response({"message":"Successful"})