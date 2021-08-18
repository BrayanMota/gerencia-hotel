from django.db import models

# Create your models here.

class Quarto(models.Model):
  quarto_id = models.AutoField(primary_key=True)
  nome = models.CharField(blank=True, null=False, max_length=30)
  numero = models.IntegerField(blank=True, null=False)
  preco = models.FloatField(blank=True, null=False)

  def __str__(self):
      return self.nome
