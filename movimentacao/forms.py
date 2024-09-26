from django import forms
from django.utils.timezone import now
from .models import Movimentacao
from pasto.models import Pasto
from lote.models import Lote


class MovimentacaoForm(forms.ModelForm):
    """Form definition for Movimentacao."""
    pasto = forms.ModelChoiceField(queryset=None)
    lote = forms.ModelChoiceField(queryset=None)
    class Meta:
        """Meta definition for Movimentacaoform."""
        model = Movimentacao
        fields = ['lote', 'pasto', 'data', 'user']

        widgets = {
            'data' : forms.DateInput(attrs={'type':'date','value': now().strftime("%Y-%m-%d")}),
            'user' : forms.HiddenInput(),
        }

    def __init__(self, user, *args, **kwargs):
        super(MovimentacaoForm, self).__init__(*args, **kwargs)
        
        self.fields['pasto'].queryset = Pasto.objects.filter(user=user)
        self.fields['lote'].queryset  = Lote.objects.filter(user=user)
        self.fields['user'].initial = user
