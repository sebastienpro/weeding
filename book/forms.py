from PIL import Image
from book.models import Page
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import ModelForm


class PageForm(ModelForm):
    #name = forms.CharField(label='Nom du ou des contributeur(s)', max_length=100)
    #content = forms.CharField(widget=CKEditorWidget())
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)

#    def save(self, *args, **kwargs):
#        if self.cleaned_data['image1']:
#            image = Image.open(self.cleaned_data['image1'])
#            image.resize((200, 200))
#            image.save(self.cleaned_data['image1']._name)
#            self.cleaned_data['image1'] = image
#        super(PageForm, self).save(*args, **kwargs)

    class Meta:
        model = Page
        fields = ['name', 'title', 'content', 'image1', 'image2']
