from django.contrib import admin
from .models import (
    Tecnologia, Competencia, Licenciatura, 
    UnidadeCurricular, Projeto, TFC, 
    Formacao, Voluntariado, MakingOf
)

# Configuração especial para as relações "Muitos para Muitos"
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    filter_horizontal = ('tecnologias', 'competencias')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    filter_horizontal = ('competencias',)

# Registo simples para todos os outros modelos
admin.site.register(Competencia)
admin.site.register(Licenciatura)
admin.site.register(UnidadeCurricular)
admin.site.register(TFC)
admin.site.register(Formacao)
admin.site.register(Voluntariado)
admin.site.register(MakingOf)