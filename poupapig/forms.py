from django import forms
from django.contrib.auth.models import User
from poupapig.models import Profile, Category
from django.contrib.auth.forms import UserCreationForm

# class CategoryForm(forms.Form):
# 	user = User
# 	name = forms.CharField(max_length=50)
# 	def clean(self):
# 		cleaned_data = super(CategoryForm, self).clean()
# 		user = cleaned_data.get('user')
# 		name = cleaned_data.get('name')
# 		if not name and not user:
# 			raise forms.ValidationError('You have to write something!')
		

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('name',)

class LoginForm(forms.Form):
	username = forms.CharField(label='Nome', max_length=100)
	password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	class Meta:
		model = User
		fields = ('username', 'birth_date', 'first_name', 'last_name', 'email', 'password1', 'password2', )
