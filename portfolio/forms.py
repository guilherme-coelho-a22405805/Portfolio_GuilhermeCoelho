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

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['nome','licenciaturas','competencias','data_inicio','data_conclusao','link_certificado','descricao']

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome','unidade_curricular','tecnologias','competencias','imagem','descricao','link_github']

class VoluntariadoForm(forms.ModelForm):
    class Meta:
        model = Voluntariado
        fields = ['nome','competencias','data_inicio','data_conclusao','descricao','certificado']