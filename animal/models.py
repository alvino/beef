from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from dateutil.relativedelta import relativedelta
from lote.models import Lote



class Animal(models.Model):
    SEXO_CHOICES = (('M',"MACHO"),('F', "FEMEA"))
    STATUS_CHOICES = (('P','PRODUTIVO'),('V','VENDIDO'),('M','MORTO'))
    """Model definition for Animal."""
    
    nome = models.CharField(max_length=50, blank=True, null=False)
    brinco = models.CharField(max_length=10, blank=True, null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='F' )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    data_change_status = models.DateField(blank=True, null=True)
    data_nascimento = models.DateField()
    mae = models.CharField(max_length=50, blank=True)
    pai = models.CharField(max_length=50, blank=True)
    descricao = models.TextField(default='',blank=True)
    lote = models.ForeignKey(Lote, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Animal."""

        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'

    def __str__(self):
        if self.brinco == None:
            return self.nome
        else:
            return str(self.brinco) 

    @property
    def get_meses(self):
        d1 = self.data_nascimento
        d2 = datetime.now()
        # diferença entre d1 e d2
        diff = relativedelta(d2, d1)
        return diff.months + (diff.years * 12)

