from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class Financeiro(models.Model):
    CAIXA_CHOICES = (('E','ENTRANDO'), ('S', 'SAINDO'))

    caixa = models.CharField(max_length=1, choices=CAIXA_CHOICES)
    descricao = models.CharField( max_length=50)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = 'Financeiro'
        verbose_name_plural = 'Financeiros'

    def __str__(self):
        return "{}".format(self.descricao)
