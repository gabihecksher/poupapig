from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(label='Nome', max_length=100)
	password = forms.CharField(label='Senha', widget=forms.PasswordInput)