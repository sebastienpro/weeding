from book.models import Page
from django import forms
from django.forms import ModelForm


class PageForm(ModelForm):
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)

    class Meta:
        model = Page
        fields = ['name', 'title', 'content', 'image1', 'image2']
