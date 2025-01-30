from django.db import models
from django.shortcuts import reverse


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=120, help_text='Enter the name of the recipe')
    ingredients = models.TextField(help_text='List all ingredients, separated by commas')
    cooking_time = models.IntegerField(help_text='Cooking time in minutes')
    description = models.TextField(help_text='Short description of the recipe')
    pic = models.ImageField(upload_to='recipes', default='recipes_no_picture.jpg')

    def __str__(self):
        return str(self.name)
    
    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients.split(','))
        if self.cooking_time < 10 and num_ingredients < 4:
            return "Easy"
        if self.cooking_time < 10 and num_ingredients >= 4:
            return "Medium"
        if self.cooking_time >= 10 and num_ingredients < 4:
            return "Intermediate"
        if self.cooking_time >= 10 and num_ingredients >= 4:
            return "Hard"
        
    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})