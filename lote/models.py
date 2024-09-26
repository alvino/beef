from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from dateutil.relativedelta import relativedelta


class Lote(models.Model):
    """Model definition for Lote."""

    nome = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Lote."""

        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'

    def __str__(self):
        return self.nome

