

# Register your models here.
from gettext import Catalog
from django.contrib import admin
from . models import Category, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)


# admin.site.register(Ingredients)