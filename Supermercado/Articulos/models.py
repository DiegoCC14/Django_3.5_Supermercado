from django.db import models

# Create your models here.

class Productos_Supermercado(models.Model):
	Nombre_Comercial = models.CharField(max_length=50 , primary_key = True)
	Categoria = models.CharField(max_length=30 , null = False) 
	Marca = models.CharField(max_length=30, null = False)
	Cantidad = models.IntegerField(default = 0)
	Peso_Litros = models.CharField(max_length=20, null = False)
	Precio = models.FloatField(max_length = 10 , default = 0.0)
	Imagen_Articulo = models.CharField(max_length=70 ,default = '')
