from django import forms
from django.utils.timezone import now
from .models import Pasto



class PastoForm(forms.ModelForm):
    """Form definition for Pasto."""

    class Meta:
        """Meta definition for Pastoform."""

        model = Pasto
        fields = ('nome','area','pastagem','user')
        labels = {'area': 'Area (ha)'}
        widgets = {
            'area': forms.NumberInput(attrs={'step':"0.10"}),
            'user': forms.HiddenInput()
        }


    def __init__(self, user, *args, **kwargs):
        super(PastoForm, self).__init__(*args, **kwargs)
        
        self.fields['pastagem'].empty_label = "Selecionar uma pastagem"
        self.fields['user'].initial = user

