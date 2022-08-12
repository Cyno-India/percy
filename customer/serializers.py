
from django.forms import JSONField
from catalog.serializers import ProductSerializer
from rest_framework import serializers
from .models import *


class OrderModelSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = OrderModel
        fields = "__all__"


class CartModelSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(many=False, read_only=True)
    
    class Meta:
        model = CartModel
        fields = ['customer_id','product_id','quantity','sub_total']
