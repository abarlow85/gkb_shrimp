from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BikeOption(models.Model):
	option = models.CharField(max_length=150)
	price_factor = models.DecimalField(max_digits=3, decimal_places=2)


	def __str__(self):
		return self.option

class WheelOption(models.Model):
	option = models.CharField(max_length=150)
	price_factor = models.DecimalField(max_digits=3, decimal_places=2)
	requisites = models.ManyToManyField(BikeOption)

	def __str__(self):
		return self.option

class BrandOption(models.Model):
	option = models.CharField(max_length=150)
	price_factor = models.DecimalField(max_digits=3, decimal_places=2)
	requisites = models.ManyToManyField(BikeOption)

	def __str__(self):
		return self.option

class CosmeticOption(models.Model):
	option = models.CharField(max_length=150)
	price_factor = models.DecimalField(max_digits=3, decimal_places=2)
	requisites = models.ManyToManyField(BikeOption)

	def __str__(self):
		return self.option

class FrameOption(models.Model):
	option = models.CharField(max_length=150)
	price_factor = models.DecimalField(max_digits=3, decimal_places=2)
	requisites = models.ManyToManyField(BikeOption)

	def __str__(self):
		return self.option

class FeaturesOption(models.Model):
	option = models.CharField(max_length=150)
	price_factor = models.DecimalField(max_digits=3, decimal_places=2)
	requisites = models.ManyToManyField(BikeOption)

	def __str__(self):
		return self.option



class Bike(models.Model):
	bike_type = models.ForeignKey(BikeOption)
	bike_wheel = models.ForeignKey(WheelOption)
	bike_brand = models.ForeignKey(BrandOption)
	bike_cosmetic = models.ForeignKey(CosmeticOption)
	bike_frame = models.ForeignKey(FrameOption)
	bike_features = models.ManyToManyField(FeaturesOption, blank=True)
	nego_factor = models.DecimalField(max_digits=3, decimal_places=2, default=1.05)
	bike_price = models.DecimalField(max_digits=6, decimal_places=2, default=200.00)

	def save(self):
		self.bike_price = 200
		print self
		price_factor = (
			self.bike_type.price_factor *
			self.bike_wheel.price_factor *
			self.bike_brand.price_factor *
			self.bike_cosmetic.price_factor *
			self.bike_frame.price_factor *
			self.nego_factor
		)

		for feature in self.bike_features.all().values():
			price_factor *= feature['price_factor']

		print price_factor


		self.bike_price *= price_factor
		print self.bike_features.all().values()
		super(Bike, self).save()
		
		 

