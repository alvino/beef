from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 
from .models import Lote
from .forms import LoteForm
from util.auth import is_data_authorized



"""Lote"""

@login_required
def loteView(request):
    lotes = Lote.objects.filter(user=request.user)
    context = {}
    context['lotes'] = lotes
    return render(request, 'loteView.html', context)


@login_required
def loteCreateView(request):
    context = {}
    form = LoteForm( )
    if request.method == 'POST':
        form = LoteForm( request.POST)
        if form.is_valid():
            lote = form.save(commit=False)
            lote.user = User.objects.filter(id=request.user.id).first()
            lote.save()    
            return redirect('/fazenda/lote')
    
    context["form"] = form
    return render(request, 'loteFormView.html', context)
       

@login_required
def loteUpdateView(request, id):
    lote = get_object_or_404(Lote, id=id)
    if(is_data_authorized(request, lote.user)):
        return redirect('/fazenda/lote')

    context = {}
    form = LoteForm(  instance=lote)

    if request.method == 'POST':
        form = LoteForm( request.POST, instance=lote)
        if form.is_valid():
            form.save()
            return redirect('/fazenda/lote')
    
    context["form"] = form
    context["lote"] = lote
    context["onDelete"] = True
    return render(request, 'loteFormView.html', context)


@login_required
def loteDeleteView(request, id):
    lote = get_object_or_404(Lote, id=id)
    if(is_data_authorized(request, lote.user)):
        return redirect('/fazenda/lote')
      
    try:
        Lote.objects.filter(id=id).delete()
    except Exception as e:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar os dados')
        
    return redirect('/fazenda/lote')

