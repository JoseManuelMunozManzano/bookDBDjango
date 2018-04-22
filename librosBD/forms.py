from django import forms
from .models import Book

class BookForm(forms.ModelForm):

	class Meta:
		model = Book
		fields = ('title', 'author', 'start_reading_date', 'end_reading_date',)
