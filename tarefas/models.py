from django.db import models
from django.contrib.auth.models import User

"""criação das informações referentes a tarefa no banco de dados"""
class TarefaModel(models.Model):
    tarefa = models.CharField(max_length=100)
    feito = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    prazo_final = models.DateTimeField(null=True, blank=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    """criação do usuário para atribuir as tarefas a um só usuário"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    """retornar as tarefas para apresentação visual"""
    def __str__(self):
        return self.tarefa