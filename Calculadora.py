# coding=utf-8

from CalculadoraCientifica import CalculadoraCientifica

calcula = CalculadoraCientifica()

x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))

print "El valor del seno de ",x," es ", calcula.seno(x)
print "El valor del coseno de ",x," es ", calcula.coseno(x)

