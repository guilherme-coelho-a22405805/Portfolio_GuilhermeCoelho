## ficheiro escola/views.py

from django.shortcuts import render
from .models import Curso, Aluno, Professor

def cursos_view(request):
    cursos=Curso.objects.all()       
    return render(request, 'escola/cursos.html', {'cursos': cursos})

def alunos_view(request):
    alunos=Aluno.objects.all()
    return render(request, 'escola/alunos.html', {'alunos': alunos})

def professores_view(request):
    professores=Professor.objects.all()
    return render(request, 'escola/professors.html',{'professores':professores})