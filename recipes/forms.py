from django import forms
from .models import Recipes, Tag


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['id', 'author', 'title', 'is_activate', 'tag']
        exclude = ['author', 'is_activate']


class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['id', 'author', 'title', 'is_activate', 'tag']
        exclude = ['author']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
