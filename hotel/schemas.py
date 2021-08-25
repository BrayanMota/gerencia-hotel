from ninja import Schema

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