from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	path('expenses', views.expense_list, name='expense_list'),
	path('new_expense', views.create_expense, name='new_expense'),
	path('categories', views.show_categories, name='show_categories'),
	path('new_category', views.create_category, name='new_category'),
	path('', views.index, name='index'),
	path('signup', views.signup, name='signup'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('profile', views.profile, name='profile'),
	path('profile/infos', views.user_infos, name='user_infos'),
	
] 