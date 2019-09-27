# coding=utf-8

from CalculadoraBasica import CalculadoraBasica
import math
import cmath

class CalculadoraCientifica(CalculadoraBasica):
	def seno(self,x):
		return math.sin(x)

	def coseno(self,x):
		return math.cos(x)

	def exponencial(self,x):
		return cmath.exp(2j*math.pi*x)
