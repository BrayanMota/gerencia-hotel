from ninja import Schema
from pydantic.utils import Obj
from datetime import date

from hotel.models import Quarto

class QuartoSchema(Schema):
  quarto_id: int
  nome: str
  numero: int
  preco: float
  camas: int
  frigobar: bool
  
  # class Meta:
  #   model = Quarto
  #   fields = '__all__'
  
class ReservaSchema(Schema):
  reserva_id: int
  quarto: QuartoSchema
  checkIn : date
  checkOut : date