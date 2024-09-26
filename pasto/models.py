from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from dateutil.relativedelta import relativedelta



class Pastagem(models.Model):

    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class Pasto(models.Model):
    """Model definition for Pasto."""
    
    nome = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=8, decimal_places=2)
    pastagem = models.ForeignKey(Pastagem, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Pasto."""

        verbose_name = 'Pasto'
        verbose_name_plural = 'Pastos'

    def __str__(self):
        return self.nome

