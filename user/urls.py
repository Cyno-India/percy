from django.urls import re_path
from user.views import *
from .loginotp import *
urlpatterns = [
    re_path(r'customerregister', CustomerRegisterView.as_view(), name='customer'),
    re_path(r'salesregister', SalesRegisterView.as_view(), name='vendor'),
    re_path(r'login_with_mobile', LoginWithMobile.as_view(), name='login_with_mobile'),
    re_path(r'login_otp', login_otp.as_view(), name='login_otp'),
    re_path(r'login_verify', verify_otp.as_view(), name='login_verify'),
    re_path(r'login', LoginView.as_view(), name='login'),
    re_path(r'logout', LogoutView.as_view(), name='logout'),
    re_path(r'profile', UserProfileView.as_view(), name='profile'),
    # re_path(r'verifyotp', VerifyOtp.as_view(), name='verifyotp')

]