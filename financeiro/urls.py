from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.financeiroView, name='financeiro'), 
    path('cadastra/', views.financeiroCreateView, name='financeiroCreate'),
    path('altera/<int:id>', views.financeiroUpdateView, name='financeiroUpdate'),
    path('delete/<int:id>', views.financeiroDeleteView, name='financeiroDelete'), 

]