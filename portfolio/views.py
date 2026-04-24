from django.shortcuts import render,redirect
from .models import Tecnologia,Competencia,Formacao,Licenciatura,Projeto,Voluntariado
from .forms import CompetenciaForm, TecnologiaForm
# Create your views here.
def main_view(request):
    return render(request, 'portfolio/index.html')


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html',{'tecnologias':tecnologias})

def tecnologia_nova_view(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')  
    else:
        form = TecnologiaForm()

    return render(request, 'portfolio/tecnologia_nova.html', {
        'form': form,
    })


def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {
        'competencias': competencias,
    })

def competencia_nova_view(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competencias')  
    else:
        form = CompetenciaForm()

    return render(request, 'portfolio/competencia_nova.html', {
        'form': form,
    })


def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request,'portfolio/formacoes.html',{'formacoes':formacoes} )

def licenciatura_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request,'portfolio/licenciatura.html',{'licenciaturas':licenciaturas} )

def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request,'portfolio/projetos.html',{'projetos':projetos} )

def voluntariado_view(request):
    voluntariados = Voluntariado.objects.all()
    return render(request,'portfolio/voluntariado.html',{'voluntariados':voluntariados} )
