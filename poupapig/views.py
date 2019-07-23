from django.shortcuts import render
from .models import Expense, Categorie
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm


def expense_list(request):
	expenses = Expense.objects.all()
	return render(request, 'expense_list.html', {'expenses': expenses})

def index(request):
	return render(request, 'index.html', {})

# def user_login(request):
# 	if request.method == 'POST':
# 		form = LoginForm(request.POST)
# 		if form.is_valid():
# 			cd = form.cleaned_data
# 			user = authenticate(username=cd['username'], password=cd['password'])
# 		if user is not None:
# 			if user.is_active:
# 				login(request, user)
# 				return HttpResponse('Authenticated', 'successfully')
# 			else:
# 				return HttpResponse('Disabled account')
# 		else:
# 			return HttpResponse('Invalid login')
# 	else:
# 		form = LoginForm()
# 	return render(request, 'poupapig/login.html', {'form':form})

def signup(request):
	if request.method == 'POST':
		print("eh post")
		form = UserCreationForm(request.POST)
		if form.is_valid():
			print("eh valido")
			form.save()
			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request, 'registration/signup.html', {'form':form})

def profile(request):
	if request.user.is_authenticated:
		return render(request, 'registration/profile.html')
	else:
		return redirect('login')