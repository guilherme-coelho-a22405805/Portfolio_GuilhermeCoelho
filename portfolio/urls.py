from django.urls import path
from . import views

urlpatterns = [
    path('tecnologias/', views.tecnologias_view, name="tecnologias"),
    path('tecnologia/nova/',views.tecnologia_nova_view, name='tecnologia_nova'),
    path('competencias/',views.competencias_view, name="competencias"),
    path('competencias/nova/', views.competencia_nova_view, name="competencia_nova"),
    path('licenciatura/',views.licenciatura_view, name="licenciatura"),
    path('formacoes/',views.formacoes_view, name="formacoes"),
    path('formacoes/nova/', views.formacoes_nova_view, name="formacoes_nova"),
    path('projetos/',views.projetos_view, name="projetos"),
    path('projetos/nova/',views.projetos_nova_view, name="projetos_nova"),
    path('voluntariado/',views.voluntariado_view, name="voluntariado"),
    path('voluntariado/nova',views.voluntariado_nova_view, name="voluntariado_nova"),
    path('', views.main_view, name='landingPage'),
]