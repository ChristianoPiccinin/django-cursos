
from django.urls import path
from . import views
urlpatterns = [
    path("acessar_curso/<int:id>", views.acessar_curso, name='acessar_curso'),
    path("desativar_curso/<int:id>", views.desativar_curso, name='desativar_curso'),
    path("deletar_curso/<int:id>", views.deletar_curso, name='deletar_curso'),
    path("criar_curso/", views.criar_curso),
    path("listar_cursos/", views.listar_cursos, name='listar_cursos')
]
