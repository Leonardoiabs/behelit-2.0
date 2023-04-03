from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Livros(models.Model):
    STATUS_CHOICES = [
        ('concluído', 'Concluído'),
        ('em andamento', 'Em andamento'),
        ('hiatus', 'Hiatus'),
        ('listado', 'Listado'),
    ]

    nome = models.CharField(max_length=200)
    genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING)
    autor = models.CharField(max_length=200)
    descricao = models.TextField()
    link = models.URLField()
    foto = models.ImageField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nome
