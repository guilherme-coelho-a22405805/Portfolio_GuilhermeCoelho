## escola/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.cursos_view, name="cursos"),
    path('alunos/',views.alunos_view, name="alunos"),
    path('professores/',views.professores_view, name="professores"),
    path('', views.cursos_view),
]