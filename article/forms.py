from django import forms
from .views import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title', 'image', 'content',
        ]
