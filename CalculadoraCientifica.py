# coding=utf-8

from CalculadoraBasica import CalculadoraBasica
import math
import cmath

class CalculadoraCientifica(CalculadoraBasica):
	def seno(self,x):
		return math.sin(x)

	def coseno(self,x):
		print "el coseno de ", x, " es: ", math.cos(x)

	def exponencial(self,x):
		print "La exponencial de ",x,"es: ",cmath.exp(2j*math.pi*x)
