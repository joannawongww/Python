from django.shortcuts import render
from django.views.generic import ListView, DetailView  # to display lists
from .models import Book  # to access book model
from django.contrib.auth.mixins import LoginRequiredMixin  # protect CBV

# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = Book  # specify model
    template_name = 'books/main.html'  # specify template


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book  # specify model
    template_name = 'books/detail.html'  # specify template
