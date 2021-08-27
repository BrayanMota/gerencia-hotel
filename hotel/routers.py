from django.urls import path
from . import viewsets
from hotel.viewsets import QuartoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter( )
router.register(r'lista_quartos', QuartoViewSet)

urlpatterns = [
    path('lista_quartos/', viewsets.lista_quartos, name='lista_quartos'),
    path('detalhes_quarto/<int:quarto_id>', viewsets.detalhes_quarto, name='detalhe_quarto'),
    path('cadastro_quarto', viewsets.cadastro_quarto, name='cadastro_quarto'),
    path('edita_quarto/<int:quarto_id>', viewsets.edita_quarto, name='edita_quarto'),
    path('exclui_quarto/<int:quarto_id>', viewsets.exclui_quarto, name='exclui_quarto'),
]