from django import forms
from rango.models import Page, Category
from django.shortcuts import redirect

class CategoryForm(forms.ModelForm):
    
    name = forms.CharField(max_length=128,
    help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    ikes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    lug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:

        model = Category
        fields = ('name',)
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
    help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
    help_text="Please enter the URL of the page.")
    varsiews = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Page
        exclude = ('category',)
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data

    



