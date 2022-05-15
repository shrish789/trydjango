from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length = 120)
	description = models.TextField(blank = True, null = True)
	price = models.DecimalField(decimal_places = 2, max_digits = 10000)
	summary = models.TextField(blank = False, null = False)
	featured = models.BooleanField() # If we want to add a column in our model then we have to give a default value to it or set null as true