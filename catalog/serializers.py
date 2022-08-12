
from django.forms import JSONField
from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Product
        fields = "__all__"


class SearchSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(many=False, read_only=True)

    
    class Meta:
        model = Product
        fields = ['item_name','strip','product_id','description','ingredients','manufactured_by','marketed_by','description_2','description_3','price','stock_status','related_products']
