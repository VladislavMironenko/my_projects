from django import  forms
from django.forms import ModelForm
from .models import *



class verification(forms.Form):
    username =forms.CharField(max_length=50)
    password = forms.CharField(min_length=5 , widget=forms.PasswordInput)

class Telegramm_Form(forms.Form):
    # username = forms.CharField(max_length=50)
    title = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description'}) , max_length=150)
    # photo = forms.ImageField()
    url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Link'}))


class Discord_Form(forms.Form):
    # username = forms.CharField(max_length=50)
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description'}) , max_length=150)
    url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Link'}))


class Telegramm_Reviews_Form(ModelForm):
    class Meta:
        model = Telegramm_Reviews
        fields = ['text', 'reporter']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Write a review'}),
        }


class Discord_Reviews_Form(ModelForm):
    class Meta:
        model = Discord_Reviews
        fields = ['text', 'reporter']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Write a review'}),
        }