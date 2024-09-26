from django import forms
from django.utils.timezone import now
from .models import Animal


class AnimalForm(forms.ModelForm):
    """Form definition for Animal."""
    
    class Meta:
        """Meta definition for Animalform."""
        model = Animal
        fields = ('nome','brinco','sexo','data_nascimento','mae','pai', 'descricao', 'user')

        widgets = {
            'data_nascimento' : forms.DateInput(attrs={'type':'date','value': now().strftime("%d/%m/%Y")}),
            'descricao': forms.Textarea(attrs={'rows':'5'}),
            'user': forms.HiddenInput(),
        }

    
    def __init__(self, user, *args, **kwargs):
        super(AnimalForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = user


    def preencidoNomeOrBrinco(self):
        if self.data.get('nome', '') != '':
            return True
        elif self.data.get('brinco', '') != '':
            return True
        else:
            self.errors['nome'] = 'Digite pelo menos um brinco'
            self.errors['brinco'] = 'Digite pelo menos um nome'
            return False

    def is_valid(self):
        return super(AnimalForm, self).is_valid()
        # # nome_or_brinco = self.preencidoNomeOrBrinco()
        # if valid and nome_or_brinco:
        #     return True
        # else:
        #     return False
