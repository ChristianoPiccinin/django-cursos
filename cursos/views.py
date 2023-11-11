from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime

from cursos.models import Curso



def inserir_curso(nome_curso, carga_horaria):
    curso = Curso(
            nome = nome_curso,
            carga_horaria = carga_horaria,
            data_criacao = datetime.now(),
            ativo = True
        )
        
    curso.save()



def deletar_curso(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, 'deletar_curso.html', {'curso': curso})

def desativar_curso(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, 'acessar_curso.html', {'curso': curso})


def acessar_curso(request, id):
    curso = Curso.objects.get(id=id)

    return render(request, 'acessar_curso.html', {'curso': curso})


def listar_cursos(request):
    filtro = request.GET.get('nome_filtrar')
    
    cursos = Curso.objects.all()
    if filtro is not None:
        cursos = Curso.objects.filter(nome__contains=filtro)
        

    return render(request, 'listar_cursos.html', {'cursos':cursos})
    
  
def criar_curso(request):
    

    if request.method == "GET":
        status = request.GET.get('status')
        return render(request, 'criar_curso.html', {'status': status})
       
    elif request.method == "POST":
        nome_curso = request.POST.get('nome_curso')
        carga_horaria = request.POST.get('carga_horaria')

        inserir_curso(nome_curso,carga_horaria)

        return redirect('/cursos/criar_curso/?status=1')
