from django.contrib import admin
from .models import Topping, Type, Food

# Register your models here.
admin.site.register(Type)
admin.site.register(Topping)
admin.site.register(Food)
