from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 
from fazenda.models import Fazenda
from .models import Animal
from .forms import AnimalForm

from util.auth import is_data_authorized


"""Animal"""

@login_required
def animalView(request):
    fazendas = Fazenda.objects.filter(user=request.user)
    ids = map(lambda fazenda: fazenda.id, fazendas)
    
    query_fazenda = Animal.objects.filter(user=request.user)
    produtivos = query_fazenda.filter( status='P')
    vendidos   = query_fazenda.filter( status='V')
    mortos     = query_fazenda.filter( status='M')
    context = {}
    context['produtivos'] = produtivos
    context['vendidos']   = vendidos
    context['mortos']     = mortos
    return render(request, 'animalView.html', context)


@login_required
def animalCreateView(request):    
    context = {}
    form = AnimalForm(request.user, request.POST or None)
    if form.is_valid():
        form.save()   
        return redirect('/animal')
    
    
    context["form"] = form
    return render(request, 'animalFormView.html', context)
       

@login_required
def animalUpdateView(request, id):
    animal = get_object_or_404(Animal, id=id)
    
    if(is_data_authorized(request, animal.user)):
        return redirect('/animal')

    context = {}
    form = AnimalForm(request.user, request.POST or None, instance=animal)
    if form.is_valid():
        form.save()
        return redirect('/animal')
    
    context["form"] = form
    context["animal"] = animal
    context["onDelete"] = True
    return render(request, 'animalFormView.html', context)


@login_required
def animalDeleteView(request, id):
    animal = get_object_or_404(Animal, id=id)
    
    if(is_data_authorized(request, animal.user)):
        return redirect('/animal')
        
    try:
        Animal.objects.filter(id=id).delete()
    except:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar os dados')
        
    return redirect('/animal')
   
