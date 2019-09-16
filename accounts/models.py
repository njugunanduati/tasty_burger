from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	country = models.CharField(max_length=100)


	def __str__(self):
		return f'{self.user.username} Profile'
