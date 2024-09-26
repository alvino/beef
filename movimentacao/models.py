from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from dateutil.relativedelta import relativedelta

from lote.models import Lote
from pasto.models import Pasto

class Movimentacao(models.Model):
    """Model definition for Movimentacao."""

    lote  = models.ForeignKey(Lote, on_delete=models.CASCADE)
    pasto = models.ForeignKey(Pasto, on_delete=models.CASCADE)
    data  = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Movimentacao."""

        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'

    def __str__(self):
        """Unicode representation of Movimentacao."""
        pass

