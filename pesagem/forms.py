from django import forms
from django.utils.timezone import now
from .models import Pesagem
from animal.models import Animal


class PesagemForm(forms.ModelForm):
    """Form definition for pesagem."""

    class Meta:
        """Meta definition for pesagemform."""

        model = Pesagem
        fields = ('animal','peso', 'data','user')
        widgets = {
            'data' : forms.DateInput(attrs={'type':'date','value': now().strftime("%d/%m/%Y")}),
            'user' : forms.HiddenInput()
        }

    def __init__(self, user, *args, **kwargs):
        super(PesagemForm, self).__init__(*args, **kwargs)
        
        self.fields['animal'].queryset = Animal.objects.filter(status='P', user=user.id)
        self.fields['data'].initial = now()
        self.fields['user'].initial = user
