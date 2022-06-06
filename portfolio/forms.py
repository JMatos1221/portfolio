from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'description']

        labels = {
            'author': 'Author',
            'title': 'Title',
            'description': 'Description',
        }

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description...'}),
        }
