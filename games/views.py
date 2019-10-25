from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import GameRentForm, GiveBackForm
from .models import GameRentModel


class RentGameView(FormView):
    template_name = 'rentGame.html'

    def get(self, request, **kwargs):
        form = GameRentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = GameRentForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            obj = GameRentModel()
            obj.guest = data['guest']
            obj.game = data['game']
            obj.save()
            form = GameRentForm()

        return render(request, self.template_name, {'form': form})


class GiveBackView(FormView):
    template_name = 'giveBackGame.html'

    def get(self, request, **kwargs):
        form = GiveBackForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = GiveBackForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            data['choice'].delete()

        return render(request, self.template_name, {'form': form})


def index(request):
    return redirect('rent')
