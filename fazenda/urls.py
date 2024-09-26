from django.urls import path
from . import views

urlpatterns = [
    path('',views.fazendaView, name='fazenda'), 
    path('cadastra/', views.fazendaCreateView, name='fazendaCreate'),
    path('altera/<int:id>', views.fazendaUpdateView, name='fazendaUpdate'),

]