from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 
from .models import Pasto
from .forms import PastoForm

from util.auth import is_data_authorized



"""Pasto"""

@login_required
def pastoView(request):
    pastos = Pasto.objects.filter(user=request.user)
    context = {}
    context['pastos'] = pastos
    return render(request, 'pastoView.html', context)


@login_required
def pastoCreateView(request):
    context = {}
    form = PastoForm(request.user, request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/pasto')

    context["form"] = form
    return render(request, 'pastoFormView.html', context)
       

@login_required
def pastoUpdateView(request, id):
    pasto = get_object_or_404(Pasto, id=id)
    
    if(is_data_authorized(request, pasto.user)):
        return redirect('/pasto')

    context = {}
    form = PastoForm(request.user, request.POST or None, instance=pasto)
    if form.is_valid():
        form.save()
        return redirect('/pasto')
    
    context["form"] = form
    context["pasto"] = pasto
    context["onDelete"] = True
    return render(request, 'pastoFormView.html', context)


@login_required
def pastoDeleteView(request, id):
    pasto = get_object_or_404(Pasto, id=id)
    if(is_data_authorized(request, pasto.user)):
        return redirect('/pasto')

    try:
        Pasto.objects.filter(id=id).delete()
    except:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar os dados')
        
    return redirect('/pasto')

