# coding=utf-8
import math
import numpy as np
def media(x,N):
	m=0;
	for i in range(N):
		m=float(x[i])+m;
	med=m/N;
	print("La media es :", float(med));
	return(med);
	

def cuadratica(x,N):
	m=0;
	for i in range(N):
		m=float(x[i]**2)+m;
	cuad=m/N;
	print("La cuadratica es :", float(cuad));
def varianza(x,n):
	m=0;
	k=0;
	for i in range(N):
		m=float(x[i])+m;
	med=m/N;
	
#	media(x,n)
	for i in range(N):
		k=(float(x[i])-med)**2 + k;
	var=k/N;
	desviacion=math.sqrt(var);
	print("Varianza: ",var, "Y la desviacion es: ", desviacion);	
N=input("Ingrese el numero de datos: ");
x=input("Ingrese el vector de datos: ");
xx=np.array(x);
media(x,N)
cuadratica(x,N)
varianza(x,N)
