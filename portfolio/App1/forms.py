from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    email = forms.CharField(validators=[EmailValidator()], widget= forms.EmailInput(attrs={'placeholder': 'abc@xyz.com', 'class': 'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message!', 'class': 'form-control'}))