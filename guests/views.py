from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import AddGuestForm, DeleteGuestForm
from .models import Guest


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
            guest.document = data['document']
            guest.city = data['city']
            guest.age = data['age']
            guest.guest_type = data['guest_type']
            guest.save()

        args = {'form': form, 'guest_id': str(guest)}

        return render(request, self.template_name, args)


class DeleteGuestView(FormView):
    template_name = 'deleteGuest.html'

    def get(self, request, guest_id=None, **kwargs):
        print(guest_id)
        if guest_id:
            guest = Guest.objects.filter(id=guest_id)
            print(guest)
            guest.delete()
            return redirect('/guests/deleteguest/')

        form = DeleteGuestForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = DeleteGuestForm(request.POST)
        args = {}

        if form.is_valid():
            try:
                guest = form.cleaned_data['guest']
                guest_type = guest[0].upper()
                guest_id = guest[1:]
                guest = Guest.objects.filter(guest_type=guest_type, id=guest_id)

                if len(guest) == 1:
                    args['is_found'] = True
                    args['guest_id'] = guest_id
                else:
                    args['guest_exist'] = False

            except ValueError as err:
                print("views.DeleteGuestView: {}".format(err))

        args['form'] = form

        return render(request, self.template_name, args)