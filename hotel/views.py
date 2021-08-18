from hotel.forms import QuartoForm
from django.shortcuts import get_object_or_404, redirect, render
from hotel.models import Quarto

# Create your views here.
def pagina_inicial(request):
  return render(request, 'pagina_inicial.html', {})

def cadastra_quarto(request):
  form = QuartoForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = QuartoForm()
  return render(request, 'cadastra_quarto.html', {'form': form})

def edita_quarto(request, quarto_id):
  quarto = get_object_or_404(Quarto, pk=quarto_id)
  form = QuartoForm(request.POST or None, instance=quarto)
  if form.is_valid():
    form.save()
  return redirect('cadastra_quarto', quarto_id=quarto.quarto_id)

def detalhes_quarto(request, quarto_id):
  quarto = get_object_or_404(Quarto, pk=quarto_id)
  return render(request, 'detalhes_quarto.html', {'quarto': quarto})

# def exclui_quarto(request, quarto_id):
#   quarto = get_object_or_404(Quarto, pk=quarto_id)
#   return render(request, 'edita_quarto.html', {'quarto': quarto})

def lista_quartos(request):
  quartos = Quarto.objects.order_by('numero')
  return render(request, 'lista_quartos.html', {'quartos': quartos})