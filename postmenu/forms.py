from django import forms
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=50, label='Заголовок поста')
    text = forms.CharField(widget=forms.Textarea(), label='Текст поста')
