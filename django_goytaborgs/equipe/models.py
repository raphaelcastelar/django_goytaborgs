from django.db import models

# Create your models here.

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    capitao = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
