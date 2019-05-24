# módulo do Django para criar urls
from django.urls import path

# Importe todas suas classes do view
from .views import *

urlpatterns = [
    #path('caminho/da/url', ClasseLáDoView.as_view(), name="nomeDessaURL")
    path('', PaginaInicialView.as_view(), name="inicio"),
    path('sobre/', SobreInicialView.as_view(), name="sobre"),
    path('contato/', ContatoInicialView.as_view(), name="contato"),
    path('curriculum/', CurriculumView.as_view(), name="curriculum"),

    path('cadastrar/estado', EstadoCreate.as_view(), name="formulario"),
]
