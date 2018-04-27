from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm


def book_list(request):
	books = Book.objects.order_by('title')
	return render(request, 'librosBD/book_list.html', {'books': books})


def book_detail(request, pk):
	book = get_object_or_404(Book, pk=pk)
	return render(request, 'librosBD/book_detail.html', {'book': book})


def book_author(request, pk):
	book = get_object_or_404(Book, pk=pk)
	books = Book.objects.filter(author=book.author).order_by('title')
	return render(request, 'librosBD/book_author.html', {'books': books, 'author': book.author})


@login_required
def book_new(request):
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			book = form.save(commit=False)
			book.save()
			return redirect('book_detail', pk=book.pk)
	else:
		form = BookForm()
	return render(request, 'librosBD/book_edit.html', {'form': form})


@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'librosBD/book_edit.html', {'form': form})


@login_required
def book_remove(request, pk):
	book = get_object_or_404(Book, pk=pk)
	book.delete()
	return redirect('book_list')
