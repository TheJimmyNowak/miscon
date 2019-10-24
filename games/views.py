from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import GameRentForm, GiveBackForm


class Rent(TemplateView):
    template_name = 'rentGame.html'

    def get(self, request):
        form = GameRentForm()
        return render(request, self.template_name, {'form': form})


class GiveBackView(TemplateView):
    template_name = 'giveBackGame.html'

    def get(self, request):
        form = GiveBackForm()
        return render(request, self.template_name, {'form': form})


def index(request):
    return redirect('rent')
