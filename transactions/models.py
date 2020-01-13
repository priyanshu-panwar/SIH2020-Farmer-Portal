from django.db import models
from users.models import Profile
from django.contrib.auth.models import User

class Transaction(models.Model):
	farmer = models.OneToOneField(Profile, on_delete=models.CASCADE)
	buyer = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.farmer.user.username} - {self.buyer.user.username}'