from django.http.response import HttpResponse
from hotel.forms import QuartoForm
from django.shortcuts import redirect, render
from .models import Quarto

# Create your views here.
def pagina_inicial(request):
  return render(request, 'pagina_inicial.html', {})

def cadastro_quarto(request):
  form = QuartoForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = QuartoForm()
  return render(request, 'cadastro_quarto.html', {'form': form})

def lista_quartos(request):
  quartos = Quarto.objects.order_by('numero')
  return render(request, 'lista_quartos.html', {'quartos': quartos})