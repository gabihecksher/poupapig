from django.urls import path
from . import views

urlpatterns = [
	path('list', views.expense_list, name='expense_list'),
	path('index', views.index, name='index'),
]