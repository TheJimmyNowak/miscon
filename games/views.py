from django.shortcuts import render


def rent(request):
    return render(request, 'rent_game.html')


def give_back(request):
    return render(request, 'giveBackGame.html')
