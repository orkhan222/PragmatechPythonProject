from django import forms
from .models import *

class ContactForm(forms.Form):
    full_name = forms.CharField(label="Your name",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'full_name'
    }))

    class ContactForm(forms.Form):
        surname = forms.CharField(label="Your surname",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'surname'
    }))

    email = forms.EmailField(label="Your email",widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'email'
    }))

   

    number = forms.CharField(label="Number",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Number'
    }))


    message = forms.CharField(label="Your message",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'message'
    }))