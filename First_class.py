# coding=utf-8
import math #Libreria para usar pi
import cmath #Libreria para números complejos
import numpy as np #libreria para usar array's

x_v1 = [9, 8, 7, 4, 5] # definición de una lista
x_v2 = [1, 8, 9, 7, 1]
x_v = np.array(x_v1) # forma de convertir una lista en un array
x_v3= np.array(x_v2)

y = input("Ingrese el primer numero: ")
x = input("Ingrese el segundo numero: ")
#si utilizo cmath aparece parte compleja en los números!

for i in range(5):
	y = math.cos(x_v[i])
	print ("El valor para el coseno de ", x_v[i] , " es: ", y)
print ""	# Salto de línea                                             



for i in range(5):
	y_v = cmath.exp(2j*math.pi*x_v[i])
	print "El valor para la exponencial de ", x_v[i], "es: ", y_v

SumaVec = x_v+x_v3
print "la suma vectorial es: ",SumaVec
