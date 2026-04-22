from django.shortcuts import render
from .models import Tecnologia,Competencia,Formacao,Licenciatura,Projeto,Voluntariado

# Create your views here.
def main_view(request):
    return render(request, 'portfolio/index.html')


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html',{'tecnologias':tecnologias})

def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request,'portfolio/competencias.html',{'competencias':competencias} )

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request,'portfolio/formacoes.html',{'formacoes':formacoes} )

def licenciatura_view(request):
    licenciatura = Licenciatura.objects.all()
    return render(request,'portfolio/licenciatura.html',{'licenciatura':licenciatura} )

def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request,'portfolio/projetos.html',{'projetos':projetos} )

def voluntariado_view(request):
    voluntariado = Voluntariado.objects.all()
    return render(request,'portfolio/voluntariado.html',{'voluntariado':voluntariado} )
