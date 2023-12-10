from django.shortcuts import render
from django.views.generic import ListView, DetailView  # to display lists
from .models import Recipe  # to access book model
# to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

# Create views here

# define homepage function
# function takes request from web app
# returns template at recipes/home.html as response


def home(request):
    return render(request, 'recipe/recipe_home.html')


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe  # specify model
    template_name = 'recipe/recipe_list.html'  # specify template


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe/recipe_detail.html'
