from django.contrib import admin
from .models import Quarto

# Register your models here.
class QuartoAdmin(admin.ModelAdmin):
  fields = ('numero', 'nome', 'preco', 'camas', 'frigobar')

admin.site.register(Quarto, QuartoAdmin)