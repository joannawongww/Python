from django.db import models

# Create your models here.

# defining Book class


class Book(models.Model):
    # book name
    name = models.CharField(max_length=120)
    # genre choice, show list downdrop, default as classic
    genre_choices = (
        ('classic', 'Classic'),
        ('romantic', 'Romantic'),
        ('comic', 'Comic'),
        ('fantasy', 'Fantasy'),
        ('horror', 'Horror'),
        ('educational', 'Educational')
    )

    genre = models.CharField(
        max_length=12, choices=genre_choices, default='classic')

    # book type, default is hardcover
    book_type_choices = (
        ('hardcover', 'Hard cover'),
        ('ebook', 'E-Book'),
        ('audiob', 'Audiobook')
    )
    book_type = models.CharField(
        max_length=12, choices=book_type_choices, default='hardcopy')

    # help_text add a tooltip which can see below form field
    price = models.FloatField(help_text='in US dollars $')

    author_name = models.CharField(max_length=120)

    def __str__(self):
        return str(self.name)
