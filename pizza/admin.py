from django.contrib import admin
from .models import Topping, Type, Food, Order, Status, Order_Item, Address

# Register your models here.
admin.site.register(Type)
admin.site.register(Topping)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(Order_Item)
admin.site.register(Status)
admin.site.register(Address)
