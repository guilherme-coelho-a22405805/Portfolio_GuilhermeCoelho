from django.urls import path
from . import views

urlpatterns = [
    path('tecnologias/', views.tecnologias_view, name="tecnologias"),
    path('tecnologia/nova/', views.tecnologia_nova_view, name='tecnologia_nova'),
    path('tecnologia/<int:id>/eliminar/', views.tecnologia_eliminar_view, name='tecnologia_eliminar'),

    path('competencias/', views.competencias_view, name="competencias"),
    path('competencias/nova/', views.competencia_nova_view, name="competencia_nova"),
    path('competencia/<int:id>/eliminar/', views.competencia_eliminar_view, name="competencia_eliminar"),

    path('licenciatura/', views.licenciatura_view, name="licenciatura"),
    path('licenciatura/<int:id>/eliminar/', views.licenciatura_eliminar_view, name="licenciatura_eliminar"),

    path('formacoes/', views.formacoes_view, name="formacoes"),
    path('formacoes/nova/', views.formacoes_nova_view, name="formacoes_nova"),
    path('formacao/<int:id>/eliminar/', views.formacao_eliminar_view, name="formacao_eliminar"),

    path('projetos/', views.projetos_view, name="projetos"),
    path('projetos/nova/', views.projetos_nova_view, name="projetos_nova"),
    path('projeto/<int:id>/eliminar/', views.projeto_eliminar_view, name="projeto_eliminar"),

    path('voluntariado/', views.voluntariado_view, name="voluntariado"),
    path('voluntariado/nova', views.voluntariado_nova_view, name="voluntariado_nova"),
    path('voluntariado/<int:id>/eliminar/', views.voluntariado_eliminar_view, name="voluntariado_eliminar"),

    path('', views.main_view, name='landingPage'),

    path('tecnologia/<int:id>/editar/', views.tecnologia_editar_view, name='tecnologia_editar'),
    path('competencia/<int:id>/editar/', views.competencia_editar_view, name='competencia_editar'),
    path('formacao/<int:id>/editar/', views.formacao_editar_view, name='formacao_editar'),
    path('projeto/<int:id>/editar/', views.projeto_editar_view, name='projeto_editar'),
    path('voluntariado/<int:id>/editar/', views.voluntariado_editar_view, name='voluntariado_editar'),
]