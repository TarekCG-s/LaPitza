from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

class Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class Food(models.Model):
    name = models.CharField(max_length=64)
    small = models.FloatField(default=0)
    large = models.FloatField(default=0)
    toppings = models.IntegerField(default=0)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type} - {self.name}'

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class Status(models.Model):
    status = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return f'{self.status}'

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city =  models.CharField(max_length=24)
    district =  models.CharField(max_length=24)
    street =  models.CharField(max_length=24)
    building_num =  models.CharField(max_length=24)
    phone = PhoneNumberField()

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.city}, {self.district} - {self.street} - {self.building_num}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    total_price = models.FloatField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    date = models.DateField(default=datetime.now)

    
    def __str__(self):
        return f'{self.user.username} - {self.address} - {self.total_price}$ - {self.status}'

class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=24)
    price = models.FloatField()
    toppings = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f'{self.food} - {self.toppings} - {self.size} - {self.price}$'
