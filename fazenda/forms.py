from django import forms
from django.utils.timezone import now
from .models import Fazenda


class FazendaForm(forms.ModelForm):
    
    class Meta:
        model = Fazenda
        fields = ['nome', 'proprietario', 'inscricao_estadual', 'endereco']

        labels = {
            'nome': 'Nome',
            'proprietario' : 'Proprietario',
            'inscricao_estadual' : 'Inscrição Estatual' ,
            'endereco' : 'Endereço' ,
        }


        widgets  ={
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'proprietario': forms.TextInput(attrs={'class':'form-control'}),
            'inscricao_estadual': forms.TextInput(attrs={'class':'form-control'}),
            'endereco': forms.TextInput(attrs={'class':'form-control'}),
        }

