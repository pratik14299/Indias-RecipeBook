from django import forms
from .models import Recipe

   
        
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control'}),
            'Discreption': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }