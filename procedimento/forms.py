from django import forms
from django.utils.timezone import now
from animal.models import Animal

from .models import Procedimento


class ProcedimentoForm(forms.ModelForm):

    # animais = forms.ModelChoiceField(
    #     queryset=None,
    #     empty_label='Animias',
    #     widget= forms.CheckboxSelectMultiple(attrs={'class':'form-check-input'})
    # )

    class Meta:
        """Meta definition for Procedimentoform."""

        model = Procedimento
        fields = ['data','procedimento','detalhe', 'animais', 'user']

        labels = {
            'data': 'Data',
            'procedimento' : 'Procedimento',
            'detalhe' : 'Detalhe' 
        }

        widgets  ={
            'data' : forms.DateInput(attrs={'class':'form-control','type':'date','value': now().strftime("%Y-%m-%d")}),
            'procedimento': forms.TextInput(attrs={'class':'form-control'}),
            'detalhe': forms.Textarea(attrs={'class':'form-control','rows':'2'}),
            'animais': forms.CheckboxSelectMultiple(attrs={'class':'form-check-input'}),
            'user': forms.HiddenInput(),
        }

   
    def __init__(self, user, *args, **kwargs):
        super(ProcedimentoForm, self).__init__(*args, **kwargs)
        
        self.fields['animais'].queryset = Animal.objects.filter(status='P', user=user.id)
        self.fields['data'].initial = now()
        self.fields['user'].initial = user
        