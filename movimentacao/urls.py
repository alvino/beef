from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.movimentacaoView, name='movimentacao'), 
    path('cadastra/', views.movimentacaoCreateView, name='movimentacaoCreate'),
    path('altera/<int:id>', views.movimentacaoUpdateView, name='movimentacaoUpdate'),
    path('delete/<int:id>', views.movimentacaoDeleteView, name='movimentacaoDelete'), 

]