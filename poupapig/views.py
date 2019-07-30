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
    categories = Category.objects.filter(user = request.user)
    expenses = Expense.objects.filter(category__in=categories)
    return render(request, 'expense_list.html', {'expenses': expenses, 'categories': categories})

def index(request):
    if request.user.is_authenticated:
        return redirect('index_profile')
    else:
        return redirect('login')

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

def show_expense(request,expense_id):
    expense = Expense.objects.filter(id=expense_id)[0]
    return render(request, 'expense.html', {'expense':expense})

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

# def show_categories(request):
# 	categories = Category.objects.all()
#     expenses  = Expense.objects.all()
#     total_per_category = []
    
#     for category in categories:
#         total = 0
#         for expense in expenses:
#             if expense.category == category:
#                 total += expense.amount
#         total_per_category.append(total) # vetor com o total gasto em cada categoria
    
#     print(total_per_category)
    
# 	return render(request, 'categories.html', {'categories': categories, 'total_per_category': total_per_category})

def show_categories(request):
    categories = Category.objects.filter(user = request.user)
    expenses = Expense.objects.all()
    total_per_category = []

    print("----------------------------")
    for category in categories:
        total = 0
        for expense in expenses:
            if expense.category == category:
                total += expense.amount
        tup = (category, total)
        print(tup)
        total_per_category.append(tup)

    print(total_per_category)
    return render(request, 'categories.html', {'total_per_category': total_per_category})

def index_profile(request):
    queryset_categories = Category.objects.filter(user = request.user) # todas as categorias do usuario
    name_categories = [obj.name for obj in queryset_categories] # lista com o nome das categorias
    
    expenses  = Expense.objects.all().order_by('date')
    
    total_per_category = []

    expenses_amount = []
    expenses_date = []
    
    expenses_per_category = []
    dates_per_category = []
    
    for category in queryset_categories:
        total = 0
        for expense in expenses:
            if expense.category == category:
                total += expense.amount
                expenses_per_category.append(expense.amount)
                dates_per_category.append(expense.date)
        expenses_amount.append(expenses_per_category)
        expenses_date.append(dates_per_category)
        total_per_category.append(total) # vetor com o total gasto em cada categoria
        expenses_per_category=[]
        dates_per_category=[]
    
    print("--------------------")
    print(expenses_amount)
    print(expenses_date)

    context = {
         'name_categories': json.dumps(name_categories),
         'total_per_category': json.dumps(total_per_category),

        # DOIS VETORES DE VETORES, UM DELES COM TODOS OS VALORES GASTOS POR CATEGORIA E O OUTRO COM AS RESPECTIVAS DATAS, TUDO ORGANIZADO POR DATA 
        #  'amounts_per_category': json.dumps(expenses_amount),
        #  'dates_per_category': json.dumps(expenses_date),
     }
    return render(request, 'index_profile.html', context)
