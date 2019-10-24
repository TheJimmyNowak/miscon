from django import forms
from .models import GameRent


class GameRentForm(forms.ModelForm):
    class Meta:
        model = GameRent
        fields = ['guest_id', 'game']


class GiveBackForm(forms.ModelForm):
    class Meta:
        model = GameRent
        fields = ['guest_id', 'game']
