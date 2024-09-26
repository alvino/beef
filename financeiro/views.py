from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 
from .models import Financeiro
from .forms import FinanceiroForm

from util.auth import is_data_authorized


@login_required
def financeiroView(request):
    financeiros = Financeiro.objects.filter(user=request.user)
    context = {}
    context['financeiros'] = financeiros
    return render(request, 'financeiroView.html', context)


@login_required
def financeiroCreateView(request):    
    context = {}
    form = FinanceiroForm(request.user, request.POST or None)
    if form.is_valid():
        form.save()   
        return redirect('/financeiro')
    
    
    context["form"] = form
    return render(request, 'financeiroFormView.html', context)
       

@login_required
def financeiroUpdateView(request, id):
    financeiro = get_object_or_404(Financeiro, id=id)
    
    if(is_data_authorized(request, financeiro.user)):
        return redirect('/financeiro')

    context = {}
    form = FinanceiroForm(request.user, request.POST or None, instance=financeiro)
    if form.is_valid():
        form.save()
        return redirect('/financeiro')
    
    context["form"] = form
    context["financeiro"] = financeiro
    context["onDelete"] = True
    return render(request, 'financeiroFormView.html', context)


@login_required
def financeiroDeleteView(request, id):
    financeiro = get_object_or_404(Financeiro, id=id)
    
    if(is_data_authorized(request, financeiro.user)):
        return redirect('/financeiro')
        
    try:
        Financeiro.objects.filter(id=id).delete()
    except:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar os dados')
        
    return redirect('/financeiro')
   
