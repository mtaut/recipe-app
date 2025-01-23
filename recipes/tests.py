from django.test import TestCase
from .models import Recipe

# Create your tests here.

class RecipeModelTest(TestCase):

    def setUpTestData():
        # set up recipe object for tests in the Recipe class
        Recipe.objects.create(        
            name='Recipe One',
            ingredients='test ingredient',
            cooking_time='10',
            description='Recipe one test description.'
        )

    def test_recipe_name(self):
        # get recipe object to test
        recipe = Recipe.objects.get(id=1)
        #get metadata for 'name' field and use it to query its data
        field_label = recipe._meta.get_field('name').verbose_name
        # compare value to the expected result
        self.assertEqual(field_label, 'name')

    def test_recipe_name_length(self):
        recipe = Recipe.objects.get(id=1)
        # get metadata for 'name' and use it to query its max_length
        max_length = recipe._meta.get_field('name').max_length
        # compare value to expected result, maximum of 120
        self.assertEqual(max_length, 120)

    def test_recipe_cooking_time_value(self):
        recipe = Recipe.objects.get(id=1)
        # test value of cooking_time
        self.assertEqual(recipe.cooking_time, 10)

    def test_recipe_description_label(self):
        recipe = Recipe.objects.get(id=1)
        # test verbose name of description field
        field_label = recipe._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')