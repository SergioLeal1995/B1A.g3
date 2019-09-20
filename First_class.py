import math
import cmath
import numpy as np

x_v = [9, 8, 7, 4, 5]
y = 10
x = 15
y = math.cos(x)
print("el resultado del coseno es: ", y)

for i in range(5):
	y_v = cmath.exp(2j*math.pi*x_v[i])
	print (y_v)
