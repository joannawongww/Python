from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=120)
    # positive integer only
    cooking_time = models.PositiveIntegerField(help_text='in mins')
    ingredients = models.CharField(
        max_length=255, help_text='separate ingredient by a comma & a space')
    description = models.TextField()

    def __str__(self):
        return str(self.name)
