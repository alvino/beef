from django.urls import path
from . import views

urlpatterns = [
  

    path('', views.movimentacaoLoteView, name='movimentacaoLote'),
    path('cadastra/<int:id>', views.movimentacaoLoteUpdateView, name='movimentacaoLoteUpdate'),

 
]