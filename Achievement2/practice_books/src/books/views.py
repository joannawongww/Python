from django.shortcuts import render
from django.views.generic import ListView, DetailView  # to display lists
from .models import Book  # to access book model

# Create your views here.


class BookListView(ListView):
    model = Book  # specify model
    template_name = 'books/main.html'  # specify template


class BookDetailView(DetailView):
    model = Book  # specify model
    template_name = 'books/detail.html'  # specify template
