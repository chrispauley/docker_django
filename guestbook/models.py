from django.db import models

class GuestEntry(models.Model):
    name = models.TextField(name='name', null=False, unique=True)
    timestamp = models.DateTimeField(auto_now=True)


class Hit(models.Model):
    pass
