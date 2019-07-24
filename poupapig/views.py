from django.shortcuts import render
from .models import Expense, Categorie, Profile
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.db import transaction


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

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})

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

# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('registration/user_infos.html')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })