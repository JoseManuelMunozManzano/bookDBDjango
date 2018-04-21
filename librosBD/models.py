from django.db import models


class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	start_reading_date = models.DateField(blank=True, null=True)
	end_reading_date = models.DateField(blank=True, null=True)

	def save_book(self):
		self.save()

	def __str__(self):
		return self.title + " " + self.author
