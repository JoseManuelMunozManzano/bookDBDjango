from django.shortcuts import render

def book_list(request):
	return render(request, 'librosBD/book_list.html', {})
