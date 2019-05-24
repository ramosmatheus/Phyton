from django.shortcuts import render

#importa o templaeView para criação de páginas simples
from django.views.generic import TemplateView

#importa todas as classes do models.py
from .models import *

#Importa função que vai chamar as urls pela função delas
from django.urls import reverse_lazy

#importa as classes view para inserir, algerar e excluir
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class PaginaInicialView(TemplateView):
    #Nome do arquivo que vai ser utilizado para renderisar esta página/método/classe
    template_name = "animais/inicio.html"

class SobreInicialView(TemplateView):
    #Nome do arquivo que vai ser utilizado para renderisar esta página/método/classe
    template_name = "animais/sobre.html"

class ContatoInicialView(TemplateView):
    template_name = "animais/contato.html"

class CurriculumView(TemplateView):
    template_name = "animais/curriculum.html"


######################################### INSERIR #########################################

class EstadoCreate(CreateView):
    #Define qual modelo para essa clasee
    model = Estado
    #Qual o html que será utilizado?
    template_name = "animais/formulario.html"
    #por onde redirecionar o usuario depois de inserir um registro
    success_url = reverse_lazy('inicio')
    #Quais campos devem aparecer no formulário?
    fields = [
        'sigla','nome'
    ]

    


