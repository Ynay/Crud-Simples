from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from core.models import User
 
# Create your views here.

# Usado para fazer a listagem dos dados do banco de dados
class ClienteList(ListView):
    model = User
    queryset = User.objects.all()
 
#Usado para criar o Usuário   
class ClienteCreate(CreateView):
    model = User
    fields = ['name', 'email']
    success_url = reverse_lazy('core:list')
  
#Usado para fazer o Update dos dados do Usuário  
class ClienteUpdate(UpdateView):
    model = User
    fields = ['name', 'email']
    success_url = reverse_lazy('core:list')
 
#Usado para mostrar detalhes dos dados do Usuário   
class ClienteDetail(DetailView):
    queryset = User.objects.all()

#Usado para deletar os dados do Usuário
class ClienteDelete(DeleteView):
    queryset = User.objects.all()
    success_url = reverse_lazy('core:list')