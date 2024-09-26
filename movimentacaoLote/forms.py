from django import forms
from django.utils.timezone import now
from lote.models import Lote
from animal.models import Animal


class MovimentacaoLoteForm(forms.Form):
    animais = forms.ModelMultipleChoiceField(
        queryset=None, 
        widget = forms.CheckboxSelectMultiple(attrs={'class':'form-check-input'}) ,
    )

    def __init__(self, user, lote, *args, **kwargs):
        super(MovimentacaoLoteForm, self).__init__(*args, **kwargs)
        
        animais_produtivos = Animal.objects.filter(status='P', user=user.id)
        self.fields['animais'].queryset = animais_produtivos
        self.fields['animais'].initial = animais_produtivos.filter(lote=lote.id)
        self.lote = lote

    
    def save(self):
        animais_selected = self.cleaned_data['animais']
        for animal in animais_selected:
            animal.lote = self.lote
            animal.save() 
        # end for

