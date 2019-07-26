from django.shortcuts import render
from .models import Expense, Category, Profile
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, CategoryForm, ExpenseForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
import json


def expense_list(request):
	expenses = Expense.objects.all()
	return render(request, 'expense_list.html', {'expenses': expenses})

def index(request):
    if request.user.is_authenticated:
        return redirect('index_profile')
    else:
        return render(request, 'index.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile(request):
	if request.user.is_authenticated:
		return redirect('index_profile')
	else:
		return redirect('login')

def user_infos(request):
	if request.user.is_authenticated:
		return render(request, 'registration/user_infos.html')
	else:
		return redirect('login')


def create_category(request):
    user = request.user
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False) # commit=False avisa pra nao colocar no BD ainda porque tem mais coisa pra adicionar
            category.user = request.user
            category.save()

            return redirect('show_categories')
    else:   
        form = CategoryForm()
    return render(request, 'new_category.html', {'form': form})

def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.user, request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(request.user)
    return render(request, 'new_expense.html', {'form': form})

def show_categories(request):
	categories = Category.objects.all()
	return render(request, 'categories.html', {'categories': categories})

def index_profile(request):
    queryset_categories = Category.objects.filter(user = request.user) # todas as categorias do usuario
    name_categories = [obj.name for obj in queryset_categories] # lista com o nome das categorias
    
    expenses  = Expense.objects.all()
    
    total_per_category = []
    for category in queryset_categories:
        total = 0
        for expense in expenses:
            if expense.category == category:
                total += expense.amount
        total_per_category.append(total) # vetor com o total gasto em cada categoria

    context = {
         'name_categories': json.dumps(name_categories),
         'total_per_category': json.dumps(total_per_category),
     }
    return render(request, 'index_profile.html', context)
