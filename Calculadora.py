# coding=utf-8
from CalculadoraCientifica import CalculadoraCientifica
import os
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
	print "8. Media"
	print "9. Media cuadratica"
	print "10. Varianza y desviación estandar"
	print " "
	return input("Indruduce la operación que deseas realizar: ")

while(True):
	opcion = menu()
	if(opcion==0):
		break
	else:
 		if(opcion>0 and opcion<8):
			x = float(input("Ingrese el valor de x: "))
			y = float(input("Ingrese el valor de y: "))
	
			if(opcion == 1):
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
			raw_input(" ")
			os.system ("clear") 
		else:
			N = input("Ingrese el numero de datos: ")
			xmed = input("Ingrese el vector de datos: ")

			if(opcion==8):
				print "El valor de la media es: ", calcula.media(xmed,N)
			elif(opcion==9):
				print "La media cuadratica es: ", calcula.cuadratica(xmed,N)
			elif(opcion==10):
				var,desviacion = calcula.varianza(xmed,N)
				print "varianza: ",var, "y desviación estandar: ",desviacion
			raw_input(" ")
			os.system ("clear") 
			else:
				print "Opción incorrecta."
print "Adios!"




