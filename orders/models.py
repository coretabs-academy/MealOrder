from django.db import models
from django.db.models import *
from meals.models import Meal
from django import forms
from decimal import Decimal

# Create your models here.


class Order(models.Model):
    PRODUCT_QUANTITY_CHOICES = tuple([(str(i), str(i)) for i in range(1, 10)])

    quantity = models.CharField(max_length=2, choices=PRODUCT_QUANTITY_CHOICES)

    order_id = models.AutoField(primary_key=True)
    # order_no = models.IntegerField(primary_key=True, default=None, null=False)
    # meal = models.ForeignKey(Meal, on_delete=DO_NOTHING, blank=True, null=True)
    meal = models.ForeignKey(Meal, on_delete=DO_NOTHING)
    ordered_at = models.DateTimeField(auto_now_add=True)
    requester = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return '{}, Quantity: {}, Requester: {}'.format(self.meal, self.quantity, self.requester)

    def total(self):
        quant = Decimal(self.quantity)
        return (quant * self.meal.price)
        # return sum( [item.product.price for item in self.items.all()] )








