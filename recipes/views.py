from django.shortcuts import render
from django.views.generic import ListView, DetailView           # to display list and details of recipes
from .models import Recipe                                       # to access Recipe model
from django.contrib.auth.mixins import LoginRequiredMixin           # protecting views
# from django.contrib.auth.decorators import login_required - shouldn't need this...
from .forms import RecipeSearchForm
from .utils import get_chart
import pandas as pd
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')  

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'

    def get_queryset(self):
        queryset = Recipe.objects.all()
        form = RecipeSearchForm(self.request.GET or None)
        
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            if search_query:
                queryset = queryset.filter(ingredients__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RecipeSearchForm(self.request.GET or None)
        context['form'] = form

        search_results = self.get_queryset()
        if search_results.exists():            
            context['search_results'] = search_results

        chart = None
        search_results = None

        # extract data as a QuerySet
        recipes = Recipe.objects.all()

        if form.is_valid():
            ingredient = form.cleaned_data.get('ingredient')         
            chart_type = form.cleaned_data.get('chart_type')
            
            if ingredient:
                recipes = recipes.filter(Q(ingredients__icontains=ingredient))

            # convert QuerySet to pandas DataFrame
            if recipes.exists() and chart_type:
                df = pd.DataFrame.from_records(
                    recipes.values('ingredients', 'cooking_time')
                )

                # passing data to create the chart
                chart = get_chart(chart_type, df)
            
            search_results = recipes
        
        context['form'] = form
        context['chart'] = chart
        context['search_results'] = search_results
        return context

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_detail.html'