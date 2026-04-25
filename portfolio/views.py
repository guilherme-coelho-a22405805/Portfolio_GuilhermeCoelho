from django.shortcuts import render,redirect
from .models import Tecnologia,Competencia,Formacao,Licenciatura,Projeto,Voluntariado
from .forms import CompetenciaForm, TecnologiaForm, FormacaoForm, ProjetoForm, VoluntariadoForm
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

def formacoes_nova_view(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formacoes')  
    else:
        form = FormacaoForm()

    return render(request, 'portfolio/formacoes_nova.html', {
        'form': form,
    })

def licenciatura_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request,'portfolio/licenciatura.html',{'licenciaturas':licenciaturas} )

def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request,'portfolio/projetos.html',{'projetos':projetos} )

def projetos_nova_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projetos')  
    else:
        form = ProjetoForm()

    return render(request, 'portfolio/projetos_nova.html', {
        'form': form,
    })

def voluntariado_view(request):
    voluntariados = Voluntariado.objects.all()
    return render(request,'portfolio/voluntariado.html',{'voluntariados':voluntariados} )

def voluntariado_nova_view(request):
    if request.method == 'POST':
        form = VoluntariadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voluntariado')  
    else:
        form = VoluntariadoForm()

    return render(request, 'portfolio/voluntariado_nova.html', {
        'form': form,
    })