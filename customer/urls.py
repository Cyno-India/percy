from django.urls import re_path
from .views import *
urlpatterns = [
    re_path(r'order', OrderView.as_view(), name='order'),
    re_path(r'cart', CartView.as_view(), name='Cart'),
    re_path(r'checkout', CheckOut.as_view(), name='Cart'),

]