import numpy as np 
import math 
from matplotlib import pyplot as plt




N=(0.2)*20.
k=(0.2)*200.
f0 = (0.2)*3000
T1 = 1./f0
Tsamp = T1/N
Fsamp = 1./Tsamp 
Fmin = -Fsamp/2
Fmax = Fsamp/2
fresolv = Fsamp/N
 
n=np.linspace(0,N-1,N)
fna = np.linspace(Fmin,Fmax-fresolv,N)
t = n/Fsamp


signal=np.cos(2.*math.pi*fna*t)
#print("el vector es:",signal)
fourier = np.fft.fft(signal)
fourier_mejor=np.fft.fftshift(fourier)
fourier_abs = np.absolute(fourier_mejor)
#signal2 = np.exp(1.j*2.*math.pi*k*n/N)
#fourier2 = np.fft.fft(signal2)
#fourier2_mejor = np.fft.fftshift(fourier2)
#fourier2_abs = np.absolute(fourier2_mejor) 
plt.plot(fna,fourier_abs)
#plt.plot(fna,fourier2_abs)

plt.show()

#plt.plot(n,signal)
#plt.show()
