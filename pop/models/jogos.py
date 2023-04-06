from django.db import models


class GeneroEletronico(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class GeneroFisico(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Plataforma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class JogosEletronicos(models.Model):
    STATUS_CHOICES = [
        ('concluído', 'Concluído'),
        ('em andamento', 'Em andamento'),
        ('hiatus', 'Hiatus'),
        ('listado', 'Listado'),
    ]

    nome = models.CharField(max_length=200)
    genero_eletronico = models.ForeignKey(GeneroEletronico, on_delete=models.DO_NOTHING)
    foto = models.ImageField()
    descricao = models.TextField()
    plataforma = models.ForeignKey(Plataforma, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)


class JogosFisicos(models.Model):
    STATUS_CHOICES = [
        ('comprado', 'Comprado'),
        ('a comprar', 'A comprar'),
        ('listado', 'Listado'),
    ]

    nome = models.CharField(max_length=200)
    genero_fisico = models.ForeignKey(GeneroFisico, on_delete=models.DO_NOTHING)
    foto = models.ImageField()
    descricao = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
