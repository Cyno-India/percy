from email.policy import default
from enum import unique
from django.db import models

# Create your models here.
# from djongo import models as models
from user.models import CustomUser
from catalog.models import Product
# Create your models here.
class OrderModel(models.Model):
    STATUS = (
            ('Accept', 'Accepted'),
            ('Reject', 'Rejected'),
            ('Pending', 'Pending'),
            ('Dispatch','Dispatched'),
            ('Cancel', 'Cancelled'),
            ('Delivered', 'Delivered')
        )
    PAY_STATUS = (
        ('None','None'),
        ('Paid','Paid'),
        ('RefundInit','RefundInit'),
        ('Refunded','Refunded')
    )
    customer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    order_status = models.CharField(choices=STATUS, max_length=10, default="Pending")
    total_price = models.FloatField(default=0.0)
    payment_id = models.CharField(max_length=30,default="")
    payment_status = models.CharField(choices=PAY_STATUS, default='None',max_length=20)
    coupon_code = models.CharField(max_length=20,default="")



    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.order_status

class CartModel(models.Model):
    customer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(max_length=10, default=0)
    sub_total=models.FloatField(max_length=10,default=0.0)
    class Meta:
        unique_together= ('customer_id','product_id')
    # data = models.JSONField(default='')
    # grand_total = models.FloatField(default=0.0)
    # coupon_code = models.CharField(max_length=20,default="")

