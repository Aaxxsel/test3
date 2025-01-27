from django import forms
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=50, label='Назвыание книги')
    text = forms.CharField(widget=forms.Textarea(), label='Описание книги')
