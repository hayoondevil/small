from os import fsdecode
from django.db import models
from django.db.models.base import Model


class Shop(models.Model):
  shop_name = models.CharField(max_length=20)
  shop_address = models.CharField(max_length=40)

class Menu(models.Model):
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  food_name = models.CharField(max_length=20)

class Order(models.Model):
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  order_date = models.DateTimeField('date ordered')
  address = models.CharField(max_length=40)
  # 도착시간
  estimated_time = models.IntegerField(default=-1)
  # 배달여부
  deliver_finish = models.BooleanField(default=0)

class Orderfood(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  food_name = models.CharField(max_length=20)