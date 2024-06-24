from django.db import models

class Tarea(models.Model):
    CATEGORIAS = (
        ('Trabajo', 'Trabajo'),
        ('Personal', 'Personal'),
        ('Otro', 'Otro'),
    )

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return self.titulo


