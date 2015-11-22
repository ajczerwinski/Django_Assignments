from django.db import models

# Create your models here.
class Interest(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateField()
	class Meta:
		db_table = 'interests'

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	age = models.IntegerField()
	occupation = models.CharField(max_length=255)
	interest = models.ForeignKey(Interest)
	created_at = models.DateField()
	class Meta:
		db_table = 'users'