from django import forms
from .models import GameRentModel


class GameRentForm(forms.ModelForm):
    class Meta:
        model = GameRentModel
        fields = ['guest', 'game']


class GiveBackForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=GameRentModel.objects.all())
