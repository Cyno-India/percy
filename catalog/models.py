from email.policy import default
from enum import auto, unique
from unicodedata import category
from unittest.mock import DEFAULT
from unittest.util import _MAX_LENGTH
# from djongo import models as models
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 50, default="")

    def __str__(self):
        return self.name

class Product(models.Model):
    STOCK_STATUS = (
        ('InStock', 'InStock'),
        ('OutStock', 'OutOfStock'),
    )
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    # category_name=models.Foreignkey(Category,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    strip=models.CharField(max_length=10,unique=True)
    description=models.TextField(max_length=50)
    # ingredients=models.CharField(max_length=20)
    ingredients=models.JSONField(default="")
    manufactured_by=models.CharField(max_length=20, default="")
    marketed_by=models.CharField(max_length=20,default="")
    price=models.CharField(max_length=10, default=0.0)
    description_2=models.TextField(max_length=50, default="")
    description_3=models.TextField(max_length=50, default="")
    stock_status=models.CharField(choices=STOCK_STATUS, max_length=10, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    related_products=models.JSONField(default="")


    class Meta:
        _use_db = 'nonrel'
        ordering = ("-created_at", )

    def __str__(self):
        return self.item_name
    
     
