from django.test import TestCase
from django.urls import reverse
from .models import Recipe

# Create your tests here.

class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up recipe object for tests in the Recipe class
        cls.recipe = Recipe.objects.create(        
            name='Recipe One',
            ingredients='test ingredient1, test ingredient2, test ingredient3, test ingredient4',
            cooking_time=11,
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
        self.assertEqual(recipe.cooking_time, 11)

    def test_recipe_description_label(self):
        recipe = Recipe.objects.get(id=1)
        # test verbose name of description field
        field_label = recipe._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_calculate_difficulty(self):
        self.assertEqual(self.recipe.calculate_difficulty(), "Hard")


class RecipeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.recipe = Recipe.objects.create(
            name="Test Recipe2",
            ingredients="test ingredient3, test ingredient4, eggs, sugar, test ingredient5",
            cooking_time=15,
            description="simple test recipe."
        )

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipes:list'))
        self.assertContains(response, "Test Recipe2")
        self.assertTemplateUsed(response, 'recipes/recipes_list.html')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipes:detail', args=[self.recipe.pk]))
        self.assertContains(response, "Test Recipe2")