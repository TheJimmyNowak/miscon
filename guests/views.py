from django.shortcuts import render
from django.views.generic import FormView
from .forms import AddGuestForm
from .models import Guest


class AddGuest(FormView):
    template_name = 'guests.html'

    def get(self, request, **kwargs):
        form = AddGuestForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = AddGuestForm(request.POST)
        guest = Guest()

        if form.is_valid():
            data = form.cleaned_data
            guest.first_name = data['first_name']
            guest.last_name = data['last_name']
            guest.document = data['document']
            guest.city = data['city']
            guest.age = data['age']
            guest.save()

        args = {'form': form, 'guest_id': guest.id}

        return render(request, self.template_name, args)
