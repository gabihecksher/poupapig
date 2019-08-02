from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
	user = models.ForeignKey('auth.User', default="", on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Expense(models.Model):
	category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, default=None)
	date = models.DateField(blank=True, null=True)
	amount = models.FloatField(null=True, blank=True, default=None)
	description = models.TextField()

	def __str__(self):
		return self.description

class Incoming(models.Model):
	amount = models.FloatField(null=True, blank=True, default=None)
	date = models.DateField(blank=True, null=True)
	description = models.TextField()

	def __str__(self):
		return self.description

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	birth_date = models.DateField(null=True, blank=True)
	account_balance = models.FloatField(null=True, blank=True, default=None)

	
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

users = User.objects.all().select_related('profile')
