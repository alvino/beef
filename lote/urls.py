from django.urls import path
from . import views

urlpatterns = [
    path('',views.loteView, name='lote'), 
    path('cadastra/', views.loteCreateView, name='loteCreate'),
    path('altera/<int:id>', views.loteUpdateView, name='loteUpdate'),
    path('delete/<int:id>', views.loteDeleteView, name='loteDelete'), 
    
]