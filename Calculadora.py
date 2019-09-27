# coding=utf-8

from CalculadoraCientifica import CalculadoraCientifica

#from restavec import restavec


calcula = CalculadoraCientifica()

def menu():
	print " "
	print " "
	print "*** CALCULADORA PYTHON ***"
	print " "
	print "Seleccion una opcion:"
	print "1. Sumar"
	print "2. Restar"
	print "3. Multiplicar"
	print "4. Dividir"
	print "5. Sen(X)"
	print "6. Cos(X)"
	print "7. Exponencial(2j*pi*x)"
	print "8. Suma Vectorial"
	print "9. Resta Vectorial"
	return input("Indruduce la operación que deseas realizar: ")

while(True):
	opcion = menu()
	if(opcion==0):
		break
	else:
 
		x = float(input("Ingrese el valor de x: "))
		y = float(input("Ingrese el valor de y: "))
	
		if (opcion == 1):
			print "La suma de ", x,"+",y ," es: ", calcula.suma(x,y)
		elif(opcion==2):
			print "La resta de ",x,"-",y," es ", calcula.resta(x,y)
		elif(opcion==3):
			print "la multiplicación de ",x,"*",y," es ", calcula.multiplicar(x,y)
		elif(opcion==4):
			print "la división de ",x,"/",y," es ", calcula.dividir(x,y)
		elif(opcion==5):
			print "El valor del seno de ",x," es ", calcula.seno(x)
		elif(opcion==6):
			print "El valor del coseno de ",x," es ", calcula.coseno(x)
		elif(opcion==7):
			print "El valor de la exponencial de ",x," es ", calcula.exponencial(x)
		
		else:
			print "Opción incorrecta."
print "Adios!"




