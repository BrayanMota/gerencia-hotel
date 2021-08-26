from hotel.models import Quarto
from hotel.forms import QuartoForm
from hotel.serializers import QuartoSerializer
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework import viewsets

# Create your views here.
def cadastra_quarto(request):
  if request.method == 'POST':
    form = QuartoForm(request.POST)
    if form.is_valid():
      quarto = form.save()
      quarto.save()
      return redirect('detalhes_quarto', quarto_id=quarto.quarto_id)
  else:
    form = QuartoForm()
  return render(request, 'cadastra_quarto.html', {'form': form})

def edita_quarto(request, quarto_id):
  quarto = get_object_or_404(Quarto, pk=quarto_id)
  if request.method == 'POST':
    form = QuartoForm(request.POST, instance=quarto)
    if form.is_valid():
      form.save()
      return redirect('detalhes_quarto', quarto_id=quarto.quarto_id)
  else:
    form = QuartoForm(instance=quarto)
  return render(request, 'edita_quarto.html', {'form': form})

def lista_quartos(request):
  quartos = Quarto.objects.order_by('numero')
  return render(request, 'lista_quartos.html', {'quartos': quartos})

def detalhes_quarto(request, quarto_id):
  quarto = get_object_or_404(Quarto, pk=quarto_id)
  return render(request, 'detalhes_quarto.html', {'quarto': quarto})

def exclui_quarto(request, quarto_id):
  quarto = get_object_or_404(Quarto, pk=quarto_id)
  quarto.delete()
  return redirect('lista_quartos')

#################################################################################

#REST FRAMEWORK
class QuartoViewSet(viewsets.ModelViewSet):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer