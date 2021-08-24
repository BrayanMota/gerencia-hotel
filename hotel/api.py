from ninja import NinjaAPI, Schema, Path
from .schemas import QuartoSchema
from .models import Quarto
from django.shortcuts import get_object_or_404

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return "Hello world"

@api.post('/lista_quartos')
def lista_quartos(request, quartos: Quarto):
  return quartos