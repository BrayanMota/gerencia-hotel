from rest_framework import serializers
from hotel.models import Quarto

class QuartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarto
        fields = ['quarto_id', 'nome', 'numero', 'preco', 'camas', 'frigobar']
        
