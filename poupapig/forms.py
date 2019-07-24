from django import forms
from django.contrib.auth.models import User
from poupapig.models import Profile
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
	username = forms.CharField(label='Nome', max_length=100)
	password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	class Meta:
		model = User
		fields = ('username', 'birth_date', 'first_name', 'last_name', 'email', 'password1', 'password2', )
