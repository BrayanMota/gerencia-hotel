from django import forms
from .models import Quarto

class QuartoForm(forms.ModelForm):
  class Meta:
    model = Quarto
    fields = ('numero', 'nome', 'preco')