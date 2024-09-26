from django.db import models
from django.contrib.auth.models import User

from animal.models import Animal

class Procedimento(models.Model):
    """Model definition for Procedimento."""

    data = models.DateField()
    procedimento = models.CharField(max_length=50)
    detalhe = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animais = models.ManyToManyField(Animal)

    class Meta:
        """Meta definition for Procedimento."""

        verbose_name = 'Procedimento'
        verbose_name_plural = 'Procedimentos'

    def __str__(self):
        return self.procedimento
