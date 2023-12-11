from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, search_view

app_name = 'recipe'

urlpatterns = [
    path('', home, name='home'),
    path("recipes/", RecipeListView.as_view(), name="recipe_list"),
    path("recipes/<pk>", RecipeDetailView.as_view(), name="recipe_detail"),
    path("search/", search_view, name='search')
]
