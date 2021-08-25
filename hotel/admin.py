from django.contrib import admin
from .models import Quarto, Reserva

# Register your models here.
class QuartoAdmin(admin.ModelAdmin):
  fields = ('numero', 'nome', 'preco', 'camas', 'frigobar')
  # fieldsets = (
  #   (None, {
  #     'fields': ('numero', 'nome', 'preco', 'camas', 'frigobar')
  #   }),
  #   ('Disponibilidade', {
  #     'fields': ('disponibilidade')
  #   })
  # )

admin.site.register(Quarto, QuartoAdmin)
admin.site.register(Reserva)