from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	path('list', views.expense_list, name='expense_list'),
	path('', views.index, name='index'),
	path('signup', views.signup, name='signup'),
	path('accounts/', include('django.contrib.auth.urls')),

	path('profile', views.profile, name='profile'),
	
] 