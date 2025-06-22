from django.db import models

class Usuario(models.Model):
    nome = models.CharField("Nome", max_length=100)
    email = models.CharField("E-mail", max_length=100)
    dataNascimento = models.DateField("Data de Nascimento")

    def __str__(self):
        return self.nome
    