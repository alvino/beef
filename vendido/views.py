from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 
from animal.models import  Animal
from .forms import AnimalVendidoForm

from util.auth import is_data_authorized



""" Vendido """


@login_required
def vendidoView(request):
    animais = Animal.objects.filter(user=request.user, status='V', data_change_status__year=datetime.now().year)
    context = {}
    context['animais'] = animais
    return render(request, 'vendidoView.html', context)


@login_required
def vendidoCreateView(request):
    context = {}
    form = AnimalVendidoForm(request.user, request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/vendido')
    
    context["form"] = form
    return render(request, 'vendidoFormView.html', context)


@login_required
def vendidoDeleteView(request, id):
    animal = get_object_or_404(Animal, id=id)
    if(is_data_authorized(request, animal.user)):
        return redirect('/vendido')

    try:
        animal = Animal.objects.filter(id=id).first()
        animal.status = 'P'
        animal.data_change_status = None
        animal.descricao = "{0}\n{1}: {2}".format(animal.descricao ,now().strftime('%d/%m/%Y'),"Desfeito a venda.")
        animal.save()
    except:
        messages.add_message(request, constants.ERROR, 'Erro ao alterar os dados')
        
    return redirect('/vendido')
