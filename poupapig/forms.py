from django import forms
from django.contrib.auth.models import User
from poupapig.models import Profile, Category, Expense, Incoming
from django.contrib.auth.forms import UserCreationForm


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('name',)

class ExpenseForm(forms.ModelForm):
	class Meta:
		model = Expense
		fields = ('category', 'date', 'amount', 'description',)
	
	def __init__(self, user, *args, **kwargs):
		super(ExpenseForm, self).__init__(*args, **kwargs)
		self.fields['category'].queryset = Category.objects.filter(user=user)

class IncomingForm(forms.ModelForm):
	class Meta:
		model = Incoming
		fields = ('amount', 'date', 'description',)

class LoginForm(forms.Form):
	username = forms.CharField(label='Nome', max_length=100)
	password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
	birth_date = forms.DateField(label="Data de nascimento", help_text='Formato: AAAA-MM-DD')
	account_balance = forms.FloatField(label="Saldo atual")
	class Meta:
		model = User
		fields = ('username', 'birth_date', 'first_name', 'last_name', 'email', 'account_balance', 'password1', 'password2', )
