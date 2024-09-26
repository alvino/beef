from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 

from .models import Pesagem
from .forms import PesagemForm


def is_data_authorized(request, user):
    if(request.user != user):
        messages.add_message(request, constants.ERROR, 'Você não tem autorização com acesso aos dados')
        return True
    else:
        return False



""" Pesagem """


@login_required
def pesagemView(request):
    pesagens = Pesagem.objects.filter(user=request.user)
    context = {}
    context['pesagens'] = pesagens
    return render(request, 'pesagemView.html', context)


@login_required
def pesagemCreateView(request):
    context = {}
    form = PesagemForm(request.user, request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/pesagem')
    
    context["form"] = form
    return render(request, 'pesagemFormView.html', context)
       

@login_required
def pesagemUpdateView(request, id):
    pesagem = get_object_or_404(Pesagem, id=id)
    
    if(is_data_authorized(request, pesagem.user)):
        return redirect('/pesagem')

    context = {}
    form = PesagemForm(request.user,  request.POST or None, instance=pesagem )
    if form.is_valid():
        form.save()
        return redirect('/pesagem')
    
    context["form"] = form
    context["pesagem"] = pesagem
    return render(request, 'pesagemFormView.html', context)


@login_required
def pesagemDeleteView(request, id):
    pesagem = get_object_or_404(Pesagem, id=id)
    if(is_data_authorized(request, pesagem.user)):
        return redirect('/pesagem')

    try:
        pesagem.objects.filter(id=id).delete()
    except:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar os dados')
        
    return redirect('/pesagem')
