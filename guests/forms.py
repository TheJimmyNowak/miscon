from django import forms
from .models import Guest


class AddGuestForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Imię'
        }
    ))
    last_name = forms.CharField(max_length=100, label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nazwisko'
        }
    ))
    city = forms.CharField(max_length=100, label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Miasto'
        }
    ))
    age = forms.IntegerField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Wiek'
        }
    ))
    document = forms.CharField(max_length=50, label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Dokument'
        }
    ))

    guest_type = forms.ChoiceField(label='', choices=Guest.types)


class DeleteGuestForm(forms.Form):
    guest = forms.CharField(max_length=50)