from django.db import models
# need connect sales with books
from books.models import Book

# Create your models here.


class Sale(models.Model):
    # book identifier
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # number of books sold
    quantity = models.PositiveIntegerField()
    # total sale price
    price = models.FloatField()
    # date of sale: auto set to current date
    date_created = models.DateTimeField(blank=True)

    def __str__(self):
        return f"id: {self.id}, book: {self.book.name}, quantity: {self.quantity}, price: {self.price}"
