from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.procedimentoView, name='procedimento'), 
    path('cadastra/', views.procedimentoCreateView, name='procedimentoCreate'),
    path('cadastra/<int:id>', views.procedimentoUpdateView, name='procedimentoUpdate'),
    path('delete/<int:id>', views.procedimentoDeleteView, name='procedimentoDelete'), 

]