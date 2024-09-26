from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 
from .models import Movimentacao
from .forms import MovimentacaoForm

from util.auth import is_data_authorized


""" Movimentacao """

@login_required
def movimentacaoView(request):
    movimentacoes = Movimentacao.objects.filter(user=request.user)
    context = {}
    context['movimentacoes'] = movimentacoes
    return render(request, 'movimentacaoView.html', context)


@login_required
def movimentacaoCreateView(request):
    context = {}
    form = MovimentacaoForm(request.user)
    if request.method == 'POST':
        form = MovimentacaoForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/movimentacao')
    
    context["form"] = form
    return render(request, 'movimentacaoFormView.html', context)
       

@login_required
def movimentacaoUpdateView(request, id):
    movimentacao = get_object_or_404(Movimentacao, id=id)
    
    if(is_data_authorized(request, movimentacao.user)):
        return redirect('/movimentacao')

    context = {}
    form = MovimentacaoForm(request.user, instance=movimentacao)

    if request.method == 'POST':
        form = MovimentacaoForm(request.user, request.POST, instance=movimentacao)
        if form.is_valid():
            form.save()
            return redirect('/movimentacao')
    
    context["form"] = form
    context["movimentacao"] = movimentacao
    context["onDelete"] = True
    return render(request, 'movimentacaoFormView.html', context)


@login_required
def movimentacaoDeleteView(request, id):
    movimentacao = get_object_or_404(Movimentacao, id=id)
    if(is_data_authorized(request, movimentacao.user)):
        return redirect('/movimentacao')

    try:
        Movimentacao.objects.filter(id=id).delete()
    except:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar os dados')
        
    return redirect('/movimentacao')

