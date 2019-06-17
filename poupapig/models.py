from django.db import models
from django.utils import timezone


class Categorie(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Expense(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, blank=True, null=True, default=None)
	date = models.DateField(blank=True, null=True)
	amount = models.FloatField(null=True, blank=True, default=None)
	description = models.TextField()

	def __str__(self):
		return self.description
