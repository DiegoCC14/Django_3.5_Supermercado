from django.shortcuts import redirect,render
from Articulos.models import Productos_Supermercado
import time

def Inicio(request):
	return redirect ('/Inicio/<0>')
def Bienvenida(request,Pagina):
	#Pagina nos indica en que pagina se encuentra. 0 seria pag 1 y haci

	Fecha = time.localtime()

	Articulos = Productos_Supermercado.objects.all()
	
	Pagina = int(Pagina[1:len(Pagina)-1])

	Cantidad_Articulos = len(Articulos)

	Lista_Productos = []
	
	#Cada pagina solo soporta 9 articulos

	for contador in range (9*Pagina,Cantidad_Articulos):
		if contador == 9*Pagina + 9:
			break
		Lista_Productos.append(Articulos[contador])

	Cantidad_Paginas = [num for num in range(int(round(Cantidad_Articulos/9+0.5)))]
	
	Contexto = {
	'Nombre_Usuario':'Diego Cazon',
	'Fecha': ' {}:{} hs - {} / {} / {}'.format(str(int(Fecha[3])-3),Fecha[4],Fecha[2],Fecha[1],Fecha[0]),
	'Temperatura':'Min 10 - Max 30',
	'Productos':Lista_Productos,
	'Cantidad_Paginas':Cantidad_Paginas
	}
	#return redirect ('/Inicio/<Pagina>')
	return render(request,'Principal.html',Contexto)

def Informacion_Producto(request,Producto):
	Producto = Producto[1:len(Producto)-1]
	Fecha = time.localtime()

	Articulo_Elegido = Productos_Supermercado.objects.filter(Nombre_Comercial=Producto)[0]
	
	Contexto = {
	'Nombre_Usuario':'Diego Cazon',
	'Fecha': ' {}:{} hs - {} / {} / {}'.format(str(int(Fecha[3])-3),Fecha[4],Fecha[2],Fecha[1],Fecha[0]),
	'Temperatura':'Min 10 - Max 30',
	'Articulo':Articulo_Elegido,
	}
	return render(request,'Informacion_Producto.html',Contexto)


