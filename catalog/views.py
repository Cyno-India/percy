from pkgutil import iter_modules
from django.http import JsonResponse
from django.shortcuts import render
from .pagination import MyLimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from user.views import authentication_user
# Create your views here.

class LogView(APIView):
    def post(self, request):
        # payload, user, user_id = authentication_user(self,request, 'customer')
        request_data = request.data
        serializer = ProductSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    def get(self, request):
        # payload, user, user_id = authentication_user(self,request, 'customer')
        # print('user_id',user_id)
        get_data = request.query_params
        print(get_data,'get_data')
        item = Product.objects.all(item_name=get_data['item_name'], strip=get_data['strip']).values('item_name','strip','description','ingredients','manufactured_by','marketed_by','description_2','description_3','price','stock_status','related_products')
        # search = Product.objects.filter(city=get_data['city'], place=get_data['place'])

        # filter_backends = (filters.DjangoFilterBackend,)
        # filterset_fields = ('strip')

        return Response(item)
        # return JsonResponse(item,safe=False)

# enerics.ListAPIView):
#     que = Product.objects.all().values('item_name','strip','description','ingredients','manufactured_by','marketed_by','description_2','description_3','price','stock_status','related_products')
#     serializers = SearchSeralizer
#     filter_backends = [SearchFilter]
#     search_fields = ['item_name']
# class GetAPI(g

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all().values()
    serializer_class = SearchSerializer
    pagination_class = MyLimitOffsetPagination 
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['item_name']
    filter_backends = [filters.SearchFilter]
    search_fields = ['strip','item_name','price']
