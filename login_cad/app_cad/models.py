from django.db import models

class Usuario(models.Model):
    Id_usuario = models.AutoField(primary_key=True)
    Nome = models.TextField(max_length=300)
    Idade = models.IntegerField()