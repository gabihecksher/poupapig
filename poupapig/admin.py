from django.contrib import admin
from .models import Expense, Category, Profile
from poupapig.models import Profile

admin.site.register(Expense)
admin.site.register(Category)
admin.site.register(Profile)
# Register your models here.
