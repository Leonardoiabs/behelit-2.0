from django.db import models


class Quadrinhos(models.Model):
    STATUS_CHOICES = [
        ('concluído', 'Concluído'),
        ('em andamento', 'Em andamento'),
        ('hiatus', 'Hiatus'),
        ('listado', 'Listado'),
    ]

    SOURCE_CHOICES = [
        ('HQ', 'HQ'),
        ('Mangá', 'Mangá'),
        ('HQ nacional', 'HQ Nacional'),
        ('Graphic Novel', 'Graphic Novel'),
    ]

    nome = models.CharField(max_length=100)
    link = models.URLField()
    descricao = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    tipo = models.CharField(max_length=30, choices=SOURCE_CHOICES)

    def __str__(self):
        return self.nome

