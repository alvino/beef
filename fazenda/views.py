from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 
from .models import Fazenda
from .forms import FazendaForm

from util.auth import is_data_authorized


"""Fazenda"""

@login_required
def fazendaView(request):
    fazenda = Fazenda.objects.filter(user=request.user).first()
    return redirect('/fazendaform/'+str(fazenda.id))

@login_required
def fazendaCreateView(request):
    context = {}
    form = FazendaForm()
    if request.method == 'POST':
        form = FazendaForm(request.POST)
        if form.is_valid():
            fazenda = form.save(commit=False)
            fazenda.user = User.objects.filter(id=request.user.id).first()
            fazenda.save()
            
            return redirect('/dashboard')
    
    context["form"] = form
    return render(request, 'fazendaFormView.html', context)
       
@login_required
def fazendaUpdateView(request, id):
    fazenda = get_object_or_404(Fazenda, id=id)
    if(is_data_authorized(request, fazenda.user)):
        return redirect('/fazenda/fazenda')

    context = {}
    form = FazendaForm(instance=fazenda)

    if request.method == 'POST':
        form = FazendaForm(request.POST,instance=fazenda)
        if form.is_valid():
            form.save()
                   
            return redirect('/dashboard')
    
    context["form"] = form
    return render(request, 'fazendaFormView.html', context)
