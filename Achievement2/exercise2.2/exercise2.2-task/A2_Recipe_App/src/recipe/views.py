from django.shortcuts import render
from django.views.generic import ListView, DetailView  # to display lists
from .models import Recipe  # to access book model
# to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
from .utils import get_recipename_from_id, get_chart

import pandas as pd

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


def search_view(request):
    form = RecipeSearchForm(request.POST or None)
    recipe_df = None  # initialize dataframe to None
    recipe_diff = None
    chart = None
    qs = None

    if request.method == 'POST':
        recipe_diff = request.POST.get('recipe_diff')
        chart_type = request.POST.get('chart_type')

        if recipe_diff == '#1':
            recipe_diff = 'Easy'
        elif recipe_diff == '#2':
            recipe_diff = 'Medium'
        elif recipe_diff == '#3':
            recipe_diff = 'Intermediate'
        elif recipe_diff == '#4':
            recipe_diff = 'Hard'

        qs = Recipe.objects.all()
        id_searched = []
        for obj in qs:
            diff = obj.calculate_difficulty()
            if diff == recipe_diff:
                id_searched.append(obj.id)

        qs = qs.filter(id__in=id_searched)

        if qs:
            recipe_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipe_df,
                              labels=recipe_df['name'].values)

            recipe_df = recipe_df.to_html()

    context = {
        'form': form,
        'recipe_df': recipe_df,
        'recipe_diff': recipe_diff,
        'chart': chart,
        'qs': qs
    }

    return render(request, 'recipe/search.html', context)
