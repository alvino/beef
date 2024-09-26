from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.vendidoView, name='vendido'),
    path('cadastra/', views.vendidoCreateView, name='vendidoCreate'),
    path('delete/<int:id>', views.vendidoDeleteView, name='vendidoDelete'),

]