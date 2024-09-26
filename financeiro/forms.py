from django import forms
from django.utils.timezone import now
from .models import Financeiro


class FinanceiroForm(forms.ModelForm):
    caixa = forms.ChoiceField(choices=Financeiro.CAIXA_CHOICES, required=True)
    class Meta:
        model = Financeiro
        fields = ('caixa','categoria','data','descricao','valor', 'user')

        widgets = {
            'data' : forms.DateInput(attrs={'type':'date'}),
            
            'user': forms.HiddenInput(),
        }

    
    def __init__(self, user, *args, **kwargs):
        super(FinanceiroForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = user
        self.fields['data'].initial = now()
        self.fields['caixa'].empty_value=None