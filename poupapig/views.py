from django.shortcuts import render
from .models import Expense, Categorie

def expense_list(request):
	expenses = Expense.objects.all()
	return render(request, 'poupapig/expense_list.html', {'expenses': expenses})

def index(request):
	return render(request, 'poupapig/index.html', {})