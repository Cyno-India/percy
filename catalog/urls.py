from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'log', LogView.as_view(), name='Log'),
    re_path(r'list', ProductList.as_view(), name='Log'),

]