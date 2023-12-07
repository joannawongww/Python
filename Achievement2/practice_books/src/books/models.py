from django.db import models
from django.shortcuts import reverse

# Create your models here.

# defining Book class
genre_choices = (
    ('classic', 'Classic'),
    ('romantic', 'Romantic'),
    ('comic', 'Comic'),
    ('fantasy', 'Fantasy'),
    ('horror', 'Horror'),
    ('educational', 'Educational')
)

book_type_choices = (
    ('hardcover', 'Hard cover'),
    ('ebook', 'E-Book'),
    ('audiob', 'Audiobook')
)


class Book(models.Model):
    # book name
    name = models.CharField(max_length=120)
    # genre choice, show list downdrop, default as classic
    genre = models.CharField(
        max_length=12, choices=genre_choices, default='classic')
    # book type, default is hardcover
    book_type = models.CharField(
        max_length=12, choices=book_type_choices, default='hardcopy')
    # help_text add a tooltip which can see below form field
    price = models.FloatField(help_text='in US dollars $')
    author_name = models.CharField(max_length=120)
    pic = models.ImageField(upload_to='books', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'pk': self.pk})
