from django.shortcuts import render

# Create views here

# define homepage function
# function takes request from web app
# returns template at recipes/home.html as response


def home(request):
    return render(request, 'recipe/recipe_home.html')
