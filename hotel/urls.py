
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('cadastro', views.cadastro_quarto, name='cadastro_quarto'),
    path('lista', views.lista_quartos, name='lista_quartos'),
]
