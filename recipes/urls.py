from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, CreateRecipeView

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('list/', RecipeListView.as_view(), name='recipes_list'),
    path('list/<pk>/', RecipeDetailView.as_view(), name='detail'),
    path('create/', CreateRecipeView.as_view(), name='create_recipe'),
]