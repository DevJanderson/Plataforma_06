from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=50)
    telefone = models.IntegerField()
    email = models.EmailField
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    caracteristica_empresa =  models.TextField()

    