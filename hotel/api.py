from ninja import NinjaAPI, Schema, Path
from .schemas import QuartoSchema
from .models import Quarto
from django.shortcuts import get_object_or_404
from typing import List

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return "Hello world"

@api.post('/cadastra_quarto')
def cadastra_quarto(request, quartos: QuartoSchema):
  quarto = Quarto.objects.create(**quartos.dict())
  return {"quarto_id": quarto.quarto_id}

@api.put("/edita_quarto/{quarto_id}")
def edita_quarto(request, quartos: QuartoSchema, quarto_id: int):
    quarto = get_object_or_404(Quarto, quarto_id=quarto_id)
    for attr, value in quartos.dict().items():
        setattr(quarto, attr, value)
    quarto.save()
    return {"editado": True}

@api.get('/lista_quartos', response=List[QuartoSchema])
def lista_quartos(request):
  quartos = Quarto.objects.order_by('quarto_id')
  return quartos

@api.get('/detalhe_quarto/{quarto_id}', response=QuartoSchema)
def detalhe_quarto(request, quarto_id: int):
  quarto = get_object_or_404(Quarto, quarto_id=quarto_id)
  return quarto

@api.delete('/deleta_quarto/{quarto_id}')
def deleta_quarto(request, quarto_id: int):
  quarto = get_object_or_404(Quarto, quarto_id=quarto_id)
  quarto.delete()
  return {'deletado': True}