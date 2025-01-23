from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=120, help_text='Enter the name of the recipe')
    ingredients = models.TextField(help_text='List all ingredients, separated by commas')
    cooking_time = models.IntegerField(help_text='Cooking time in minutes')
    description = models.TextField(help_text='Short description of the recipe')

    def __str__(self):
        return str(self.name)
