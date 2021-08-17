from django.db import models

# Create your models here.

class Quarto(models.Model):
  nome = models.CharField(blank=True, null=True, max_length=30)
  numero = models.IntegerField(blank=True, null=True)
  preco = models.FloatField(blank=True, null=True)
