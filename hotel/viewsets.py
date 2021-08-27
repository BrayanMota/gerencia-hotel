from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from hotel.serializers import QuartoSerializer
from hotel.models import Quarto
from rest_framework.response import Response
from rest_framework.decorators import api_view

#VERBOS DO PROTOCOLO HTTP EM APENAS UMA CLASSE
class QuartoViewSet(viewsets.ModelViewSet):
  queryset = Quarto.objects.all()
  serializer_class = QuartoSerializer

#VERBOS DO PROTOCOLO HTTP SEPARADOS EM MÉTODOS
@api_view(['GET'])
def lista_quartos(request):
  quartos = Quarto.objects.all()
  serializer = QuartoSerializer(quartos, many=True)
  return Response(serializer.data)
  
@api_view(['GET'])
def detalhes_quarto(request, quarto_id):
  quartos = Quarto.objects.all()
  quarto = get_object_or_404(quartos, pk=quarto_id)
  serializer = QuartoSerializer(quarto, many=False)
  return Response(serializer.data)
  
@api_view(['POST'])
def cadastro_quarto(request):
  serializer = QuartoSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edita_quarto(request, quarto_id):
  quarto = Quarto.objects.get(quarto_id=quarto_id)
  serializer = QuartoSerializer(quarto, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def exclui_quarto(request, quarto_id):
  quarto = Quarto.objects.get(quarto_id=quarto_id)
  quarto.delete()
  return Response('Apagado')
    