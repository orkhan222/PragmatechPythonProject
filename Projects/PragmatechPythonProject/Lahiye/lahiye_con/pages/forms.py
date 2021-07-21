from django import forms
from django.db.models import fields
from .models import Contact

class ContactForm(forms.ModelForm):


    class Meta:
        model= Contact
        fields= (
            'full_name',
            'surname',
            'email',
            'number',
            'message',
        )

        widgets= { 
            'full_name':forms.TextInput(attrs={
                'class':'form-control', 'placeholder':'Your firstname',
            }),
            'surname': forms.TextInput(attrs={
                'class':'form-control', 'placeholder':'Your lastname',
            }),
             'email': forms.EmailInput (attrs={
                'class':'form-control', 'placeholder':'E-mail',
            }),
             'number': forms.TextInput(attrs={
                'class':'form-control', 'placeholder':'Number',
            }),
             'message': forms.Textarea(attrs={
                'class':'form-control', 'placeholder':'Message',
            }),
    
    
    
    }
















    # full_name = forms.CharField(label="Your name",widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'full_name'
    # }))

    # surname = forms.CharField(label="Your surname",widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'surname'
    # }))



    # email = forms.EmailField(label="Your email",widget=forms.EmailInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'email'
    # }))

   

    # number = forms.CharField(label="Number",widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Number'
    # }))


    # message = forms.CharField(label="Your message",widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'message'
    # }))