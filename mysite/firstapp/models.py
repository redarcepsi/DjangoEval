from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    information = models.TextField()
    date = models.DateTimeField()

    participants = models.ManyToManyField(User, blank=True)

    def nb_inscrit(self):
        return self.participants.count()