from django.db import models

class List(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en_proceso','En Proceso'),
        ('completo', 'Completo'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Create your models here.
