# models.py
from django.db import models



class product_data(models.Model):
    product_name = models.CharField(max_length=20)
    product_model_name = models.CharField(max_length=20)
    product_colour=models.CharField(max_length=20)
    product_price=models.IntegerField()