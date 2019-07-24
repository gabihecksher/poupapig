from django.shortcuts import render
from .models import Expense, Category, Profile
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.db import transaction


def expense_list(request):
	expenses = Expense.objects.all()
	return render(request, 'expense_list.html', {'expenses': expenses})

def index(request):
    if request.user.is_authenticated:
        return redirect('profile')
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
		return render(request, 'registration/profile.html')
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

def show_categories(request):
	categories = Category.objects.all()
	return render(request, 'categories.html', {'categories': categories})
