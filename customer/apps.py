from django.apps import AppConfig


class CustomerConfig(AppConfig):
    name = 'customer'
#  try:
#             CartModel.objects.update(quantity=request.data['quantity'])
#         except BaseException as err:
#             print(f"Unexpected {err}, {type(err)}") 
#         return Response('Cart updated')