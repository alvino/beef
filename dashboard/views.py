from django.shortcuts import render ,redirect, get_object_or_404
from django.db.models import Count, Sum, Q
from django.contrib.auth.decorators import login_required

from datetime import datetime
from functools import reduce
from .util import animal_tabela_meses

from fazenda.models import Fazenda
from animal.models import Animal
from lote.models import Lote
from pasto.models import Pasto
from financeiro.models import Financeiro

@login_required
def dashboardView(request):
    fazenda = Fazenda.objects.filter(user=request.user).first()
    
    if fazenda == None:
        return redirect('/fazenda/cadastra')

    
    pastos = Pasto.objects.filter(user=request.user)
    sum_area = Pasto.objects.filter(user=request.user).aggregate(sum=Sum("area"))
    
    year = datetime.now().year
    animais = Animal.objects.filter(user=request.user, status='P').order_by('lote')
    animais_vendido = Animal.objects.filter(user=request.user, status='V', data_change_status__year=datetime.now().year)
    animais_morto   = Animal.objects.filter(user=request.user, status='M', data_change_status__year=datetime.now().year)
    count_animal_produtivo = animais.count()
    count_animal_morto = animais_morto.count()
    count_animal_vendido = animais_vendido.count()
    lotes = Lote.objects.filter(user=request.user)
    financeiro = Financeiro.objects.filter(user=1).aggregate( despesa=Sum('valor', filter=Q(caixa='S')) , receita=Sum('valor', filter=Q(caixa='E')) )
    financeiro_categorias = Financeiro.objects.filter(user=1).values('categoria__descricao').annotate( valor=Sum('valor') )

    context = {}
    context = {**context,**financeiro}
    context['financeiro_categorias'] = financeiro_categorias
    context['fazenda'] = fazenda
    context['ano'] = year
    context['pastos'] = pastos
    context['area'] = sum_area
    context['animais'] = animais
    context['count_animal_morto']  = count_animal_morto
    context['count_animal_vendido'] = count_animal_vendido
    context['lotes'] = lotes
    if count_animal_produtivo == 0:
        context['percentual_mortalidade'] = 0
        context['percentual_descarte'] = 0
    else:
        context['percentual_mortalidade'] = count_animal_morto/count_animal_produtivo
        context['percentual_descarte']= count_animal_vendido/count_animal_produtivo
    categoria = {}
    categoria = animal_tabela_meses(animais)
    return render(request, "dashboard.html", context={**context,**categoria})

