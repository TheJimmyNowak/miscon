from django.db import models


class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str("{}.{} {}".format(self.id, self.first_name, self.last_name))
