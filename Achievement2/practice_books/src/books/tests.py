from django.test import TestCase

# Create your tests here.
# import Book model first
from .models import Book

# class to write test


class BookModelTest(TestCase):
    # initialize fixed variable
    def setUpTestData():
        # set up non-modified object used by all test
        Book.objects.create(name='Pride and Prejudice', author_name='Jane Austen',
                            genre='classic', book_type='hardcover', price='23.71')

    # test if book's name initialized as expected
    def test_book_name(self):
        # get book object to test
        book = Book.objects.get(id=1)

        # get metadata for 'name' field and query its data
        field_label = book._meta.get_field('name').verbose_name

        # compare value to expected result
        self.assertEqual(field_label, 'name')

    # test if author_name field is max 120 char
    def test_author_name_max_length(self):
        # get book object to test
        book = Book.objects.get(id=1)

        # get metadata for 'author name' field and query its max length
        max_length = book._meta.get_field('author_name').max_length

        # compare value to expected result
        self.assertEqual(max_length, 120)

    # test if load first object brings to first object details
    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), '/books/list/1')
