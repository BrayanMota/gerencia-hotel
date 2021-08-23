from django.db import models

# Create your models here.

class Quarto(models.Model):
  quarto_id = models.AutoField(primary_key=True)
  nome      = models.CharField(blank=False, null=False, max_length=30)
  numero    = models.IntegerField(blank=False, null=False)
  preco     = models.FloatField(blank=False, null=False)
  camas     = models.IntegerField(blank=False, null=False)
  frigobar  = models.BooleanField(default=False, blank=False, null=False)

  def __str__(self):
      return self.nome
