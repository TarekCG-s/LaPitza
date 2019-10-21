from django.db import models

# Create your models here.
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
