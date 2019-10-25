from django.db import models
from guests.models import Guest


class GameRentModel(models.Model):
    guest = models.ForeignKey(Guest, models.CASCADE)
    game = models.CharField(max_length=200)

    def __str__(self):
        return self.game + ":" + self.guest.first_name
