from rest_framework import serializers
from hotel.models import Quarto

class QuartoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quarto
        fields = ['quarto_id', 'nome', 'numero', 'preco', 'camas', 'frigobar']
        
class TesteSerializer(serializers.ModelSerializer):
  apt = 't'