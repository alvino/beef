from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.pesagemView, name='pesagem'), 
    path('cadastra/', views.pesagemCreateView, name='pesagemCreate'),
    path('altera/<int:id>', views.pesagemUpdateView, name='pesagemUpdate'),
    path('delete/<int:id>', views.pesagemDeleteView, name='pesagemDelete'), 

]