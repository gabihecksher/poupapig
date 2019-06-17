from django.shortcuts import render
from .models import Expense, Categorie
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def expense_list(request):
	expenses = Expense.objects.all()
	return render(request, 'poupapig/expense_list.html', {'expenses': expenses})

def index(request):
	return render(request, 'poupapig/index.html', {})

def user_login(request):
	if request.method == 'POST':
		console.log("eh post")
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse('Authenticated', 'successfully')
			else:
				return HttpResponse('Disabled account')
		else:
			return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	return render(request, 'poupapig/login.html', {'form':form})