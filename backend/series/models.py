from django.db import models


class Serie(models.Model):

    titulo = models.CharField(max_length=100)

    genero = models.CharField(max_length=50)

    temporadas = models.IntegerField()

    STATUS_CHOICES = [
        ('ASSISTINDO', 'Assistindo'),
        ('FINALIZADA', 'Finalizada'),
        ('ABANDONADA', 'Abandonada')
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    nota = models.DecimalField(
        max_digits=3,
        decimal_places=1
    )

    def __str__(self):
        return self.titulo