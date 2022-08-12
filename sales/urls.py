"""sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # re_path(r'event-admin/', event_admin_site.urls),
    re_path(r'admin/', admin.site.urls),
    re_path(r'percy/user/', include('user.urls')),
    re_path(r'percy/catalog/', include('catalog.urls')),
    re_path(r'percy/customer/', include('customer.urls')),


    # re_path(r'api/vendor/', include('vendor.urls')),
    # re_path(r'api/customer/', include('customer.urls')),
    # re_path(r'api/delivery/', include('delivery.urls')),
    # re_path(r'api/location/', include('location.urls')),
    # re_path(r'api/dev/', include('developer.urls')),
    # re_path(r'api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # re_path(r'dash/',include("django.contrib.auth.urls")),
    # re_path(r'dashboard',views.indexView,name="index"),
    # re_path(r'changepassword',views.changepassword,name='changepassword')



]
