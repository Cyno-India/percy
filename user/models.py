from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser




# from djongo import models as models


class CustomUser(AbstractUser):
    ROLES = (
        ('sales', 'Sales'),
        ('customer', 'Customer'),
    )
    email = models.EmailField(null=True, unique=True)
    phone = models.CharField(max_length=10, null=True , unique=True)
    address=models.CharField(max_length=20,default="")
    city = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    gst=models.CharField(max_length=20,default="")
    role = models.CharField(choices=ROLES, max_length=10)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['email','phone'],name='unique_user')
    #     ]

    def __str__(self):

        return self.email



# from django.dispatch import receiver
# from django.urls import reverse
# from django_rest_passwordreset.signals import reset_password_token_created
# from django.core.mail import send_mail  


# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

#     email_plaintext_message = f"Use this token to reset your password \n \n {reset_password_token.key}"

#     send_mail(
#         # title:
#         "Password Reset for {title}".format(title="Skyrath"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "info.skyrath@gmail.com",
#         # to:
#         [reset_password_token.user.email]
#     )