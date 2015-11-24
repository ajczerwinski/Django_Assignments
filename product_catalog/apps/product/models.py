from django.db import models
from datetime import datetime


# Create your models here.
class Manufacturer(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateField()
	class Meta:
		db_table = 'manufacturers'

class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	description = models.CharField(max_length=255)
	manufacturer = models.ForeignKey(Manufacturer)
	created_at = models.DateTimeField(datetime.now())
	class Meta:
		db_table = 'products'
