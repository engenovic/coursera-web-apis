from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal

#Starter Serializer
# class MenuItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MenuItem
#         fields = ['id','title','price','inventory']

# #Normal Serializer
# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6,decimal_places=2)
#     inventory = serializers.IntegerField()

#Model Serializer
class CategorySerilizer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory') # Change inventory to stock field
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
   # category = serializers.StringRelatedField() # Relationship Serializer
    category = CategorySerilizer(read_only=True) # On GET only
    category_id = serializers.IntegerField(write_only=True) # On POst only    
    class Meta:
        model = MenuItem
        fields = ['id','title','category','price','stock','price_after_tax','category_id']
    def calculate_tax(self,product:MenuItem): # Add calculated fields to the serializer
        return product.price * Decimal(1.1)