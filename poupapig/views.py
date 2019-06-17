from django.shortcuts import render

def expense_list(request):
	return render(request, 'poupapig/expense_list.html', {})
