from django import forms
from django.utils.timezone import now
from .models import Lote


class LoteForm(forms.ModelForm):
    """Form definition for Lote."""

    class Meta:
        """Meta definition for Loteform."""
        model = Lote
        exclude = ['user']
