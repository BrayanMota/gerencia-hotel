
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('cadastra/', views.cadastra_quarto, name='cadastra_quarto'),
    path('detalhes/<int:quarto_id>/', views.detalhes_quarto, name='detalhes_quarto'),
    path('edita/<int:quarto_id>/', views.edita_quarto, name='edita_quarto'),
    path('lista/', views.lista_quartos, name='lista_quartos'),
]
