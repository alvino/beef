from django import forms
from django.utils.timezone import now
from animal.models import Animal



class AnimalVendidoForm(forms.Form):
    data = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}))
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3'}))
    animais = forms.ModelMultipleChoiceField(
        queryset=None, 
        widget = forms.CheckboxSelectMultiple(attrs={'class':'form-check-input'}),
    )
    
    def __init__(self, user, *args, **kwargs):
        super(AnimalVendidoForm, self).__init__(*args, **kwargs)
        
        self.fields['animais'].queryset = Animal.objects.filter(status='P', user=user.id)
        self.fields['data'].initial = now()
        
    def save(self):
        animais_selected = self.cleaned_data['animais']
        data = self.cleaned_data['data']
        descricao = self.cleaned_data['descricao']
        for animal in animais_selected:
            animal.status = 'V'
            animal.data_change_status = data
            animal.descricao = "{0}\n{1}: {2}".format(animal.descricao, data.strftime('%d/%m/%Y'), descricao)
            animal.lote = None
            animal.save() 
        # end for

