from books.models import Book

# function that takes ID


def get_bookname_from_id(val):
    # used to retrieve name from record
    bookname = Book.objects.get(id=val)
    # return name
    return bookname
