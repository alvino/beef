from django.urls import path
from . import views

urlpatterns = [
  
    path('',views.pastoView, name='pasto'), 
    path('cadastro/', views.pastoCreateView, name='pastoCreate'),
    path('altera/<int:id>', views.pastoUpdateView, name='pastoUpdate'),
    path('delete/<int:id>', views.pastoDeleteView, name='pastoDelete'), 

]