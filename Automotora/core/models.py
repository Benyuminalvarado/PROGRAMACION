from django.db import models
from django.contrib.auth.models import User

class Autos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='autos/')
    oferta = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    auto = models.ForeignKey(Autos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    class Meta:
        unique_together = ('usuario', 'auto')
