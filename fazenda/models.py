from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from dateutil.relativedelta import relativedelta


class Fazenda(models.Model):
    """Model definition for Fazenda."""

    nome = models.CharField(max_length=50)
    proprietario = models.CharField(max_length=150)
    inscricao_estadual = models.CharField( max_length=20)
    endereco = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Fazenda."""

        verbose_name = 'Fazenda'
        verbose_name_plural = 'Fazendas'

    def __str__(self):
        return self.nome
