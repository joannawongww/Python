from django.test import TestCase

# Create your tests here.
# import User model first
from .models import Recipe
from .forms import RecipeSearchForm

# class to write test


class RecipeModelTest(TestCase):
    # initialize fixed variable
    def setUpTestData():
        # set up non-modified object used by all test
        Recipe.objects.create(name='Tea',
                              cooking_time='5',
                              ingredients='Tea Leaves, Water, Sugar',
                              description='A yummy hot cup of tea. Add tea leaves and sugar to hot water.')

    # test if name field initialised
    def test_name_field(self):
        # get user object to test
        recipe = Recipe.objects.get(id=1)

        # get metadata for 'name' field and query its name
        name_field_label = recipe._meta.get_field('name').verbose_name

        # compare value to expected result
        self.assertEqual(name_field_label, 'name')

    # test if recipe name field is max 120 char
    def test_name_max_length(self):
        # get user object to test
        recipe = Recipe.objects.get(id=1)

        # get metadata for 'username' field and query its max length
        max_length = recipe._meta.get_field('name').max_length

        # compare value to expected result
        self.assertEqual(max_length, 120)

    # test ingredients field max length
    def test_ingredients_max_length(self):
        # get user object to test
        recipe = Recipe.objects.get(id=1)

        # get metadata for 'name' field and query its name
        max_length = recipe._meta.get_field('ingredients').max_length

        # compare value to expected result
        self.assertEqual(max_length, 255)

    # test get absolute url
    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/recipes/1')


class RecipeSearchFormTest(TestCase):
    def test_get_difficulty(self):
        form_data = {"recipe_diff": "Easy", "chart_type": "#2"}
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
