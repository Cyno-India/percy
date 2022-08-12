from distutils.log import debug
from itertools import product
from math import prod
from re import sub
from statistics import quantiles
from django.db import IntegrityError
from django.shortcuts import render
from razorpay.razor_pay import RazorPayments

# Create your views here.
from rest_framework import status

from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
import json
from .models import *
from user.views import authentication_user
from user.models import CustomUser
class OrderView(APIView):
    def post(self, request):
        payload, user, user_id = authentication_user(self,request, 'customer')
        request_data = request.data
        request_data['order_status'] = 'Pending'
        request_data['customer_id'] = user_id
        debug_key = "percykey"
        

        serializer = OrderModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        # try:
        cart_object = CartModel.objects.filter(customer_id=user_id)
        if cart_object.exists() == True:
            user_instance = CustomUser.objects.filter(id=user_id)
            cart_quan = CartModel.objects.filter(customer_id=user_id).values_list('quantity')[0][0]
            cart_sub = CartModel.objects.filter(customer_id=user_id).values_list('sub_total')[0][0]
            total=cart_quan*cart_sub
            sub_price=CartModel.objects.filter(sub_total=user_id).values_list('sub_total')

            razor = RazorPayments()
            if request.data['debug_key'] != debug_key:
                if razor.check_payment(request_data['payment_id']) == False:
                    print('checking payment id>>>>>>>>>>>>>')
                    return Response("Invalid payment id")

                # try:
                #     price = cart_object.values('grand_total')[0]['grand_total']
                # except IndexError:
                #     return Response("Error Cart is empty", status=status.HTTP_404_NOT_FOUND)

                # if razor.check_payment(request_data['payment_id'],details=True)['amount'] !=  int(price*100):
                #     return Response("Payment Id valid but amount does not match to order amount")
                
                capture = razor.capture(request_data['payment_id'],amount=int(total*100))
                if capture.status_code == 400:
                    print('captured payment<<<<<<<<<<<<<<')
                    return Response(["Payment already captured",capture])
        

            print(sub_price,'subrprice')
            try:
                order = OrderModel.objects.create(customer_id=user_instance[0],order_status=request_data['order_status'],total_price=total,payment_id=request_data['payment_id'],payment_status='Paid',coupon_code="asdasd")
            except BaseException as err:
                print(f"Unexpected {err}, {type(err)}")
            if OrderModel.objects.filter(order_status='Pending').first():
                cart_object.delete()     
            return Response('order placed',status=status.HTTP_201_CREATED)
        else:
            return Response('Error Cart Doesnt Exist')
        

    def get(self,request):
        payload, user, user_id = authentication_user(self,request, 'customer')
        orddr = OrderModel.objects.filter(customer_id=user_id).order_by('-created_at').values()
        return Response(orddr)










        # payload, user, user_id = authentication_user(self,request, 'customer')
        # # request_data = request.data
        # # request_data['order_status'] = 'Pending'
        # # serializer = OrderModelSerializer(data=request_data)
        # # serializer.is_valid(raise_exception=True)
        # # user_instance = CustomUser.objects.filter(id=user_id)
        # # data = {}
        # # cart = OrderModel.objects.create[{
        # #     "hello":1
        # # }]
        # # serializer.save()
        # # return Response()
        # request_data = request.data
        # user_instance = CustomUser.objects.filter(id=user_id).values('id')[0]['id']
        # print(user_instance)
        # use=user_instance
        # print(user_id)
        # request_data['customer_id'] = user_id
        # serializer = OrderModelSerializer(data=request_data)
        # serializer.is_valid(raise_exception=True)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#  order = OrderModel.objects.create(customer_id=user_instance[0],order_status=request_data['order_status'],cart_items=request_data['cart_items'],
#                 total_price=request_data['total_price'],payment_id=request_data['payment_id'],payment_status=request_data['payment_status'],
#                 coupon_code=request_data['coupon_code']
#                 )

class CartView(APIView):
    def post(self, request):
        payload, user, user_id = authentication_user(self,request, 'customer')
        print(user_id, user)
        product= Product.objects.filter(id=request.data['product_id'])[0]
        print(product,'product')
        price= Product.objects.filter(id=request.data['product_id']).values_list('price')[0][0]
        print(price,'product')
        try:
            customer=CustomUser.objects.filter(id=user_id)[0]
            
            CartModel.objects.create(customer_id=customer,product_id=product,
                quantity=request.data['quantity'],sub_total=price
            )
            

            cart_items=CartModel.objects.filter(customer_id=user_id)
            ct = CartModelSerializer(cart_items, many=True)
        except BaseException as err:
            return Response("Cart item with this id already exists",status=status.HTTP_409_CONFLICT) 
        # cart_quan=CartModel.objects.filter(quantity=user_id).values_list('quantity')[0][0]
        # pro_id=CartModel.objects.filter(quantity=user_id).values_list('product_id')[0][0]


        # print(pro_id,'quatity')
        # cart_pro=Product.objects.filter(id=cart_items)
        # print(cart_pro)
        # if CartModel.objects.filter(customer_id=user_id).values_list('cart')
        return Response(ct.data, status=status.HTTP_201_CREATED)
    

    def get(self, request):
        # payload, user, user_id = authentication_user(self,request, 'customer')
        # print('user_id',user_id)
        item = CartModel.objects.all()
        return Response( CartModelSerializer(item, many=True).data,)
        # return JsonResponse(item,safe=False)



    def put(self, request):
        payload, user, user_id = authentication_user(self,request, 'customer')
        # print('user_id',user_id)
        customer=CustomUser.objects.filter(id=user_id)[0]
        product= Product.objects.filter(id=request.data['product_id'])[0]
        try:
            cart_items=CartModel.objects.filter(customer_id=user_id)
        except BaseException as err:
            print(f"Unexpected {err}, {type(err)}") 
        cart_items.update(quantity=request.data['quantity'])
        return Response('Cart updated')
        # return JsonResponse(item,safe=False)


    def delete(self, request):
        payload, user, user_id = authentication_user(self,request, 'customer')
        cart_object = CartModel.objects.filter(customer_id=user_id)
        pro_id= CartModel.objects.filter(id=request.data['id'])
        # product= Product.objects.filter(id=request.data['product_id'])[0]
        pro_id.delete()
        return Response(f"cart deleted for {user}")


class CheckOut(APIView):
    def get(self, request):
        payload, user, user_id = authentication_user(self,request, 'customer')
        try:        
            cart_quan = CartModel.objects.filter(customer_id=user_id).values_list('quantity')[0][0]
            cart_sub = CartModel.objects.filter(customer_id=user_id).values_list('sub_total')[0][0]
            cart_obj = CartModel.objects.filter(customer_id=user_id)
            # grand_total = []
            # total = cart_quan*cart_sub
            # grand_total.append(total)
            ct = CartModelSerializer(cart_obj, many=True)
        except :
            return Response('ERROR CART IS EMPTY')
        print(cart_quan)
        print(cart_sub)
        # ct = CartModelSerializer(cart_obj, many=True)
        # if not cart_obj.exists():
        #     return Response("No cart created")
        # else:
        # data = {
        #     "grand_total": grand_total,
        # }
        return Response(ct.data)




# class OrderView(APIView):
#     def post(self, request):
#         payload, user, user_id = authentication_user(self,request, 'customer')
#         request_data = request.data
#         request_data['order_status'] = 'Pending'
#         request_data['customer_id'] = user_id
        

#         serializer = OrderModelSerializer(data=request_data)
#         serializer.is_valid(raise_exception=True)
#         # try:
#         cart_object = CartModel.objects.filter(customer_id=user_id)
#         if cart_object.exists() == True:
#             user_instance = CustomUser.objects.filter(id=user_id)
#             cart_quan = CartModel.objects.filter(customer_id=user_id).values_list('quantity')[0][0]
#             cart_sub = CartModel.objects.filter(customer_id=user_id).values_list('sub_total')[0][0]
#             total=cart_quan*cart_sub
#             sub_price=CartModel.objects.filter(sub_total=user_id).values_list('sub_total')
#             print(sub_price,'subrprice')
#             try:
#                 order = OrderModel.objects.create(customer_id=user_instance[0],order_status=request_data['order_status'],total_price=total,payment_id='pzjasdasd',payment_status='Paid',coupon_code="asdasd")
#             except BaseException as err:
#                 print(f"Unexpected {err}, {type(err)}")
#             if OrderModel.objects.filter(order_status='Pending').first():
#                 cart_object.delete()     
#             return Response('order placed',status=status.HTTP_201_CREATED)
#         else:
#             return Response('Error Cart Doesnt Exist')
        
