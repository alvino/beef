from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 

from .models import Procedimento
from .forms import ProcedimentoForm

from util.auth import is_data_authorized


@login_required
def procedimentoView(request):
    procedimentos = Procedimento.objects.filter(user=request.user)
    context = {}
    context['procedimentos'] = procedimentos
    return render(request, 'procedimentoView.html', context)


@login_required
def procedimentoCreateView(request):
    context = {}
    form = ProcedimentoForm(request.user, request.POST or None)
    print(form.is_valid())
    if form.is_valid():
        
        procedimento = form.save()
        procedimento.animias = form.cleaned_data['animais']
        procedimento.save()
        return redirect('/procedimento')
    
    context["form"] = form
    return render(request, 'procedimentoFormView.html', context)
       

@login_required
def procedimentoUpdateView(request, id):
    procedimento = get_object_or_404(Procedimento, id=id)
    
    if(is_data_authorized(request, procedimento.user)):
        return redirect('/procedimento')

    context = {}
  
    form = ProcedimentoForm(request.user, request.POST or None, instance=procedimento)
    if form.is_valid():
        form.save()
        return redirect('/procedimento')
    
    context["form"] = form
    context["procedimento"] = procedimento
    context["onDelete"] = True
    return render(request, 'procedimentoFormView.html', context)


@login_required
def procedimentoDeleteView(request, id):
    procedimento = get_object_or_404(Procedimento, id=id)
    
    if(is_data_authorized(request, procedimento.user)):
        return redirect('/procedimento')

    try:
        Procedimento.objects.filter(id=id).delete()
    except:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar os dados')
        
    return redirect('/procedimento')

