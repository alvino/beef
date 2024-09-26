from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.mortoView, name='morto'),
    path('cadastra/', views.mortoCreateView, name='mortoCreate'),
    path('delete/<int:id>', views.mortoDeleteView, name='mortoDelete'),
]