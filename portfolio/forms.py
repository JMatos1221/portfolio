from django import forms
from django.forms import ModelForm
from .models import TFC, Post


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


class TFCForm(ModelForm):
    class Meta:
        model = TFC
        fields = '__all__'

        labels = {
            'github_link': 'Github',
            'youtube_link': 'Youtube',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'advisor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Advisor'}),
            'resume': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Resume...'}),
            'github_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Github Link'}),
            'youtube_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Youtube Link'}),
            'report_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Report Link'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),

        }
