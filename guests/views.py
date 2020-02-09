from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import AddGuestForm, DeleteGuestForm
from .models import Guest
from games.models import GameRentModel


class AddGuestView(FormView):
    template_name = 'addGuest.html'

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
            guest.city = data['city']
            guest.age = data['age']
            guest.save()

        args = {'form': form, 'guest_id': str(guest)}

        return render(request, self.template_name, args)


class DeleteGuestView(FormView):
    template_name = 'deleteGuest.html'

    def get(self, request, guest_id=None, **kwargs):
        if guest_id:
            rented_games = GameRentModel.objects.filter(guest_id=guest_id)
            if len(rented_games) == 0:
                guest = Guest.objects.filter(id=guest_id)
                guest.delete()
                return redirect('/guests/deleteguest/')
            else:
                print("NIE ODDANA GRA!!! " + str(rented_games))
                return redirect('gamenotcommited')

        form = DeleteGuestForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = DeleteGuestForm(request.POST)
        args = {}

        if form.is_valid():
            try:
                guest_id = int(form.cleaned_data['guest'])
                guest = Guest.objects.filter(id=guest_id)

                if len(guest) == 1:
                    args['is_found'] = True
                    args['guest_id'] = guest_id
                else:
                    print("Guest doesn't exist guests/views.py")
                    args['guest_exist'] = False

            except ValueError as err:
                print("views.DeleteGuestView: {}".format(err))

        args['form'] = form

        return render(request, self.template_name, args)


def game_not_committed_view(request):
    return render(request, 'gameNotCommitted.html')
