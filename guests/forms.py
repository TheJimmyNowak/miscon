from django import forms


class AddGuestForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    age = forms.IntegerField()
    document = forms.CharField(max_length=50)

    guest_type = forms.ChoiceField(choices=[
        ('participant', 'Uczestnik'),
        ('guest', 'Gość'),
        ('volunteer', 'Wolontariusz')]
    )
