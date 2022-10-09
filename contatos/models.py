from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.


class Contato(models.Model):

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_Length=255)
    email = models.CharField(max_Length=255, blank=True)
    data_criacap = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True)
