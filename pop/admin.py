from django.contrib import admin
from pop.models import Quadrinhos, Genero, Livros, GeneroEletronico, GeneroFisico, JogosEletronicos, JogosFisicos


admin.site.register(Genero)
admin.site.register(GeneroEletronico)
admin.site.register(GeneroFisico)
admin.site.register(JogosEletronicos)
admin.site.register(JogosFisicos)
