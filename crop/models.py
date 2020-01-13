from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Types(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Unit(models.Model):
	name = models.CharField(max_length=100)
	value = models.IntegerField()

	def __str__(self):
		return self.name

class Crop(models.Model):
	farmer = models.OneToOneField(User, on_delete=models.CASCADE)
	cat = models.ForeignKey('Category', on_delete=models.CASCADE)
	name = models.ForeignKey('Types', on_delete=models.CASCADE)
	quantity = models.IntegerField()
	unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)
	pickup = models.CharField(max_length=200)
	image = models.ImageField(upload_to='crop', null=True, blank=True)
	date_posted = models.DateField(default=timezone.now)

	def __str__(self):
		return f'{self.farmer} - {self.date_posted}'