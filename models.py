from django.db import models

class Size(models.Model):
	
	SIZES = [
   	('SMALL', 60),
    ('MIDDLE', 120),
   	('BIG', 180),
    ]

	name = models.CharField(max_length=50)
	size = models.CharField(choices=SIZES, max_length=20)
	
	def __str__(self):
		return self.name


class Discount(models.Model):
	add_type = models.CharField(max_length=30)
	amount = models.IntegerField()
	def __str__(self):
		return self.name

class Ingredient(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	def __str__(self):
		return self.name

class Pizza(models.Model):
	name = models.CharField(max_length=50)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)
	discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
	ingridients = models.ManyToManyField(Ingredient, blank=True, null=True)
	price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	def __str__(self):
		return self.name

class Drink(models.Model):
	name = models.CharField(max_length=50)
	prise = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	def __str__(self):
		return self.name
		
		

		