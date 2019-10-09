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
	
	def media(self,xmed,N):
		m=0
		for i in range(N):
			m=float(xmed[i])+m
		med=m/N
		med = float(med)
		return med

	def cuadratica(self,xmed,N):#media cuadratica
		m=0;
		for i in range(N):
			m=float(xmed[i]**2)+m;
		cuad=m/N;
		cuad = float(cuad)
		return cuad

	def varianza(self,xmed,N):
		m=0;
		k=0;
		for i in range(N):
			m=float(xmed[i])+m;
		med=m/N;
		for i in range(N):
			k=(float(xmed[i])-med)**2 + k;
		var=k/N;
		desviacion=math.sqrt(var);
		return var,desviacion
