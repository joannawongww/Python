from django.shortcuts import render
from django.views.generic import ListView, DetailView  # to display lists
from .models import Recipe  # to access book model

# Create views here

# define homepage function
# function takes request from web app
# returns template at recipes/home.html as response


def home(request):
    return render(request, 'recipe/recipe_home.html')


class RecipeListView(ListView):
    model = Recipe  # specify model
    template_name = 'recipe/recipe_list.html'  # specify template


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe/recipe_detail.html'
