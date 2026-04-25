from django.shortcuts import render,redirect
from .models import Tecnologia,Competencia,Formacao,Licenciatura,Projeto,Voluntariado
from .forms import CompetenciaForm, TecnologiaForm, FormacaoForm, ProjetoForm, VoluntariadoForm


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


### VIEWS PARA O DELETE ----------------------------------
def tecnologia_eliminar_view(request, id):
    tecnologia = Tecnologia.objects.get(id = id)
    if request.method == 'POST':
        tecnologia.delete()
    return redirect('tecnologias')

def competencia_eliminar_view(request, id):
    competencia = Competencia.objects.get(id = id)
    if request.method == 'POST':
        competencia.delete()
    return redirect('competencias')

def formacao_eliminar_view(request, id):
    formacao = Formacao.objects.get(id = id)
    if request.method == 'POST':
        formacao.delete()
    return redirect('formacoes')

def licenciatura_eliminar_view(request, id):
    licenciatura = Licenciatura.objects.get(id = id)
    if request.method == 'POST':
        licenciatura.delete()
    return redirect('licenciatura')

def projeto_eliminar_view(request, id):
    projeto = Projeto.objects.get(id = id)
    if request.method == 'POST':
        projeto.delete()
    return redirect('projetos')

def voluntariado_eliminar_view(request, id):
    voluntariado = Voluntariado.objects.get(id = id)
    if request.method == 'POST':
        voluntariado.delete()
    return redirect('voluntariado')



### VIEWS DE EDIÇÃO -------------------------------------------
def tecnologia_editar_view(request, id):
    tecnologia = Tecnologia.objects.get(id = id)
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)

    return render(request, 'portfolio/tecnologia_editar.html', {
        'form': form,
        'tecnologia': tecnologia,
    })


def competencia_editar_view(request, id):
    competencia = Competencia.objects.get(id = id)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)

    return render(request, 'portfolio/competencia_editar.html', {
        'form': form,
        'competencia': competencia,
    })


def formacao_editar_view(request, id):
    formacao = Formacao.objects.get(id = id)
    if request.method == 'POST':
        form = FormacaoForm(request.POST, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm(instance=formacao)

    return render(request, 'portfolio/formacao_editar.html', {
        'form': form,
        'formacao': formacao,
    })


def projeto_editar_view(request, id):
    projeto = Projeto.objects.get(id = id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'portfolio/projeto_editar.html', {
        'form': form,
        'projeto': projeto,
    })


def voluntariado_editar_view(request, id):
    voluntariado = Voluntariado.objects.get(id = id)
    if request.method == 'POST':
        form = VoluntariadoForm(request.POST, request.FILES, instance=voluntariado)
        if form.is_valid():
            form.save()
            return redirect('voluntariado')
    else:
        form = VoluntariadoForm(instance=voluntariado)

    return render(request, 'portfolio/voluntariado_editar.html', {
        'form': form,
        'voluntariado': voluntariado,
    })