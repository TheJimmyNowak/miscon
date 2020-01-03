from django.db import models


class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    pesel = models.CharField(max_length=50)
    types = (
        ('U', 'Uczestnik'),
        ('G', 'Gość'),
        ('W', 'Wolontariusz'),
        ('O', 'Organizator')
    )
    guest_type = models.CharField(max_length=1, default='O')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.guest_type) + str(self.id)
