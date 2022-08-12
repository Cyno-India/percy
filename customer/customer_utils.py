# from catalog.models import Catalog
# # from razor.razor_pay import RazorPayments

# def remove_item_and_validation(data_dictionaries,vendor_id):
#     for items in data_dictionaries:
#         if check_item_in_menu(items['item_id'],vendor_id):
#             return False
#         if items['item_quantity'] <= 0:
#             data_dictionaries.remove(items)
#     return data_dictionaries            

# def check_item_in_menu(item_data,catalog_id):
#     vendor_menu_item_ids = Catalog.objects.filter(catalog_id=).values_list('item_id')

#     vendor_menu_list = [x[0] for x in vendor_menu_item_ids]
#     if item_data not in vendor_menu_list:
#         # print("check True")
#         return True
#     else:
#         print("check False")
#         return False

# def get_total_price(data):
#     price = 0.0
#     for i in data:
#         price += i['item_price'] * i['item_quantity']

#     return price

# def razor_refund(payment_id,amount): 
#     refund = RazorPayments()
#     res = refund.normal_refund(payment_id=payment_id,amount=amount)
#     return res
