from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class PaginaInicialView(TemplateView):
    #Nome do arquivo que vai ser utilizado para renderisar esta página/método/classe
    template_name = "inicio.html"

class SobreInicialView(TemplateView):
    #Nome do arquivo que vai ser utilizado para renderisar esta página/método/classe
    template_name = "sobre.html"

class ContatoInicialView(TemplateView):
    template_name = "contato.html"
