from django.db import models

# Create your models here.

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('A', 'Alta'),
        ('M', 'Media'),
        ('B', 'Baixa')
    ]
    titulo = models.CharField(max_length = 30, null = False, blank = False)
    descricao = models.CharField(max_length = 100, null = False, blank = False)
    data_expiracao = models.DateField(null = False, blank = False),
    prioridade =
