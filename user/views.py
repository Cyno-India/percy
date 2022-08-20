import re
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
# from matplotlib.style import available

from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
import json
from .models import *
from rest_framework. exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Create your views here.
import jwt, datetime


def authentication_user(self,request, role, privacy='private'):
    token = request.COOKIES.get('jwt')
    
    if not token:
        raise AuthenticationFailed('Unauthenticated, not a token')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        if privacy == 'public':
            user = CustomUser.objects.filter(id=payload['id']).first()
        else:
            user = CustomUser.objects.filter(id=payload['id'], role=role).first()

            
        
        if user is None:
            raise AuthenticationFailed("Unauthenticated, not a user")
        user_id = CustomUser.objects.filter(email=user).values_list('id')[0][0]
            
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated, expired token')

    return payload, user, user_id
## Registering vendor using UserSerializer created in Serializers.py

# class CustomerRegisterView(APIView):
#     def post(self, request):
#         request_data = request.data
#         request_data['role'] = 'customer'
#         serializer = CustomerSerializer(data=request_data)
#         serializer.is_valid(raise_exception=True)
#         serializer=CustomerModelSerializer(data=request_data)
#         # request_data['address'] = ''
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         id = serializer.data['id']
#         se = CreateCustomerModel(data={"id":id})
#         se.is_valid(raise_exception=True)
#         se.save()
#         return Response(serializer.data , status=status.HTTP_201_CREATED)


class CustomerRegisterView(APIView):
    def post(self, request):
        request_data = request.data
        request_data['role'] = 'customer'
        serializer = CustomerSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)


class SalesRegisterView(APIView):
    def post(self, request):
        request_data = request.data
        request_data['role'] = 'sales'
        serializer = SalesSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()
        if CustomUser.objects.filter(email=email).values_list('is_active')[0][0] == False:
        # print('active',active)
            return Response('Admin approval still pending')

        # if active == 'False':
        #     print('hello')
        #     return Response('Admin approval pending')
        # active = CustomUser.objects.filter(is_active=user)
        # print(active,'active')

        # if active == False:
        #     return Response('Admin Approval is still Required')


        elif user is None:
            # raise AuthenticationFailed('Credentials not found')
            return JsonResponse({"error":"Email Mismatch"}, status=401)
        
        elif not user.check_password(password):
            # raise AuthenticationFailed('Incorrect Password')
            return JsonResponse({"error":"Incorrect passoword"}, status=401)
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=7200),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret',algorithm='HS256')
        


        response =  Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data= {
            'jwt' : token
        }

        return response




class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logged Out'
        }
        return response

class UserProfileView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')
        print(token,'token')
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated !')
        
        user = CustomUser.objects.filter(id=payload['id']).first()
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

# class CreateCustomerModel(serializers.ModelSerializer):
#     class Meta:
#         model = CustomerModel
#         fields = '__all__'

#     def create(self,data):
#         instance = self.Meta.model(**data)
#         instance.save()
#         return instance