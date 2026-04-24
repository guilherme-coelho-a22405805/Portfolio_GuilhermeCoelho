from django import forms
from .models import Competencia, Tecnologia, Formacao, Licenciatura, Projeto, Voluntariado

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'tipo', 'descricao']  

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome','logo','link','rating','descricao','aspetos_relevantes','competencias']