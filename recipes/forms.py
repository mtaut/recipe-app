from django import forms

class RecipeSearchForm(forms.Form):
    ingredient = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(
        choices=[('#1', 'Bar chart'), ('#2', 'Pie chart'), ('#3', 'Line chart')],
        required=False,        
    )
