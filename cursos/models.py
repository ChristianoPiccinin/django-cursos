from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    