from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
# from matplotlib.style import available

from rest_framework.views import APIView
# from vendor.models import VendorModel
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
import json
from .models import *
from rest_framework. exceptions import AuthenticationFailed
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated

import jwt
import datetime

import base64
import json

import requests



def send_sms(mobile):
    url_endpoint = f'https://api.authkey.io/request?authkey=97363050591f50bc&mobile={mobile}&country_code=91&sid=4703&time=10'
    response = requests.get(url_endpoint)
    print('response')
    # print(response)
    print(response.content)
    # response = b'{"Status":"Success","Details":"95dc91bb-e6f4-4fcc-9163-eea370bcde14"}'
    return json.loads(response.content.decode('utf8'))


def verify_sms(otp, LogID):
    url_endpoint = f'https://authkey.io/api/2fa_verify.php?authkey=97363050591f50bc&channel=sms&otp={otp}&logid={LogID}'
    response = requests.get(url_endpoint)
    return json.loads(response.content.decode('utf8'))



def authentication_vendor(self,request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated !')

    user = CustomUser.objects.filter(id=payload['id']).first()
    user_id = CustomUser.objects.filter(phone=user).values_list('id')[0][0]
        
    return payload, user, user_id

class verify_otp(APIView):
    def post(self, request):
        LogID = request.data.get('LogID')
        otp = request.data.get('otp')

        response = verify_sms(otp, LogID)
        return JsonResponse({'msg': response}, status=200)


class login_otp(APIView):
    def post(self, request):
        mobile = request.data.get('mobile')
        if mobile is None or len(mobile) != 10:
            return JsonResponse({'error': 'Please enter your 10 digit mobile number'}, status=422)

        response = send_sms(mobile)
        return JsonResponse({'msg': response}, status=200)


class LoginWithMobile(APIView):
    def post(self,request):
        mobile = request.data.get('mobile')
        # print('mobile', mobile)
        user = CustomUser.objects.filter(phone=mobile).first()
        # print(user)

        if user is None:
            raise AuthenticationFailed('Credentials not found')
        # print(user)
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=7200),
            'iat': datetime.datetime.utcnow()
        }
        print(payload)
        token = jwt.encode(payload, 'secret',algorithm='HS256')
        # print(token)


        response =  Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data= {
            'jwt' : token
        }

        return response
