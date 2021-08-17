from hotel.forms import QuartoForm
from django.shortcuts import redirect, render
from .models import Quarto

# Create your views here.
def pagina_inicial(request):
  return render(request, 'pagina_inicial.html', {})

def cadastro_quarto(request):
  if request.method == 'POST':
    form = QuartoForm(request.POST)
    if form.is_valid():
      quarto = form.save(commit=False)
      quarto.salvar()
      return redirect('lista_quartos')

def lista_quartos(request):
  quartos = Quarto.objects.order_by('numero')
  return render(request, 'lista_quartos.html', {'quartos': quartos})