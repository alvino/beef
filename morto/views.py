from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 
from animal.models import Animal
from .forms import AnimalMortoForm

from util.auth import is_data_authorized


""" Morto """


@login_required
def mortoView(request):
    animais = Animal.objects.filter(user=request.user, status='M', data_change_status__year=datetime.now().year)
    context = {}
    context['animais'] = animais
    return render(request, 'mortoView.html', context)


@login_required
def mortoCreateView(request):
    context = {}
    form = AnimalMortoForm(request.user, request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/morto')
    
    context["form"] = form
    return render(request, 'mortoFormView.html', context)
    

@login_required
def mortoDeleteView(request, id):
    animal = get_object_or_404(Animal, id=id)
    if(is_data_authorized(request, animal.user)):
        return redirect('/morto')

    try:
        animal = Animal.objects.filter(id=id).first()
        animal.status = 'P'
        animal.data_change_status = None
        animal.descricao = "{0}\n{1}: {2}".format(animal.descricao ,now().strftime('%d/%m/%Y'),"Desfeito a morte.")
        animal.save()
    except:
        messages.add_message(request, constants.ERROR, 'Erro ao alterar os dados')
        
    return redirect('/morto')

