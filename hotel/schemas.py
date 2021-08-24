from ninja import Schema

class QuartoSchema(Schema):
  nome: str
  numero: int
  preco: float
  camas: int
  frigobar: bool