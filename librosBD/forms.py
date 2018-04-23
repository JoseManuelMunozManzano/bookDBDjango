from django import forms
from .models import Book


#class DateInput(forms.DateInput):
#	input_type = 'date'


class BookForm(forms.ModelForm):

	class Meta:
		model = Book
		fields = ('title', 'author', 'start_reading_date', 'end_reading_date',)
		labels = {
			"title": "Título",
			"author": "Autor",
			"start_reading_date": "Fecha inicio de lectura",
			"end_reading_date": "Fecha fin de lectura",
		}
		#widgets = {
		#	"start_reading_date": DateInput(),
		#	"end_reading_date": DateInput(),
		#}
