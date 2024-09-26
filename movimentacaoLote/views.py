from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 
from lote.models import Lote
from .forms import MovimentacaoLoteForm

from util.auth import is_data_authorized


""" Movimentacao Lote """


@login_required
def movimentacaoLoteView(request):
    lotes = Lote.objects.filter(user=request.user)
    context = {}
    context['lotes'] = lotes
    return render(request, 'movimentacaoLoteView.html', context)


@login_required
def movimentacaoLoteCreateView(request):
    context = {}
    form = MovimentacaoForm(request.user)
    if request.method == 'POST':
        form = MovimentacaoForm(request.user, request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)    
            movimentacao.user = User.objects.filter(id=request.user.id).first()
            movimentacao.save()
            return redirect('/movimentacaoLote')
    
    context["form"] = form
    return render(request, 'movimentacaoLoteFormView.html', context)
       

@login_required
def movimentacaoLoteUpdateView(request, id):
    lote = get_object_or_404(Lote, id=id)
    
    if(is_data_authorized(request, lote.user)):
        return redirect('/movimentacaoLote')

    context = {}
    form = MovimentacaoLoteForm(request.user, lote, request.POST or None )
    if form.is_valid():
        form.save()
        return redirect('/movimentacaoLote')
    
    context["form"] = form
    context["lote"] = lote
    return render(request, 'movimentacaoLoteFormView.html', context)


@login_required
def movimentacaoLoteDeleteView(request, id):
    movimentacao = get_object_or_404(Movimentacao, id=id)
    if(is_data_authorized(request, movimentacao.user)):
        return redirect('/movimentacaoLote')

    try:
        Movimentacao.objects.filter(id=id).delete()
    except:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar os dados')
        
    return redirect('/movimentacaoLote')

