from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	path('list', views.expense_list, name='expense_list'),
	path('', views.index, name='index'),
	path('login', views.user_login, name='user_login'),
] 