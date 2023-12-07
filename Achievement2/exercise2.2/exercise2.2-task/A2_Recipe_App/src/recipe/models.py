from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=120)
    # positive integer only
    cooking_time = models.PositiveIntegerField(help_text='in mins')
    ingredients = models.CharField(
        max_length=255, help_text='separate ingredient by a comma & a space')
    description = models.TextField()
    # added in pic field for recipe
    # gives user better idea of what kind of food it is
    pic = models.ImageField(upload_to='recipe', default='no_picture.jpg')

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 10 and len(ingredients) < 4:
            difficulty = 'Easy'
        elif self.cooking_time < 10 and len(ingredients) >= 4:
            difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(ingredients) < 4:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = 'Hard'
        return difficulty

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('recipe:recipe_detail', kwargs={'pk': self.pk})
