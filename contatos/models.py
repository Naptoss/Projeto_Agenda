from email.policy import default
from django.db import models
from django.utils import timezone
from unittest.util import _MAX_LENGTH

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=255)


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
