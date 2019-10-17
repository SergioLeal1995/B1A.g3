import numpy as np
import math
from matplotlib import pyplot as plt
from numpy import linalg as LA
 
# Parametros de la senal analiada
f=2500.
Fsamp= 20000. # la frecuencia de muestreo
# La senal discreta 
N=200
k=90
n=np.linspace(0,N-1,N)
t=n/Fsamp
signal=np.cos(2.*math.pi*f*t)
fourier=np.fft.fft(signal)
fourier_mejor=np.fft.fftshift(fourier)

#******
fourier_mejor_abs=np.power(np.absolute(fourier_mejor),2.)

#complex signal
signal_ex=np.exp(1.j*2.*math.pi*k*f*t)#verificar
fourier_ex=np.fft.fft(signal_ex)
fourier_mejor_ex=np.fft.fftshift(fourier_ex)

#******
fourier_mejor_ex_abs=np.power(np.absolute(fourier_mejor_ex),2.)
 
# calculos para relacional la senal discreta con el mundo real
Fmin=-Fsamp/2.
Fresol=Fsamp/N
Fmax=-Fmin-Fresol
f=np.linspace(Fmin,Fmax,N)
 
plt.plot(f,fourier_mejor_abs)

plt.plot(f,fourier_mejor_ex_abs)
plt.show()

