from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.animalView, name='animal'), 
    path('cadastra/', views.animalCreateView, name='animalCreate'),
    path('altera/<int:id>', views.animalUpdateView, name='animalUpdate'),
    path('delete/<int:id>', views.animalDeleteView, name='animalDelete'), 

]