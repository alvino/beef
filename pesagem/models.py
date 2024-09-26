from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from dateutil.relativedelta import relativedelta

from animal.models import Animal


class Pesagem(models.Model):
    """Model definition for Pesagem."""

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    peso = models.IntegerField()
    data = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Pesagem."""

        verbose_name = 'Pesagem'
        verbose_name_plural = 'Pesagems'

