import numpy as np
import matplotlib.pyplot as plt


T_0 = 0.01
T = 0.02
f = 1/T
A = 5
simlen = 1e3
R = 1e3; #10 k resistance
C = 10e-6;#10 uF capacitance

 #generating points in t-axis

t = np.linspace(0,0.1,simlen); #generating points in t-axis

for n in range(21):
	if n == 0:
		g = A*T_0/T;
	else:
		an = 2*A*np.sin(2*np.pi*n*f*T_0)/(2*np.pi*n*f*T); #Computing coefficients
		bn = 2*A*(1 - np.cos(2*np.pi*n*f*T_0))/(2*np.pi*n*f*T); #Computing coefficients
		s = 1j*2*np.pi*n*f;
		den = np.polyval([1, -5, 6, 1],s*C*R);
		Hn = 1/den; #Frequency response
		thetan = np.angle(Hn);


		cost = np.cos(2*np.pi*n*f*t + thetan);#Computing cosine term
		sint = np.sin(2*np.pi*n*f*t+ thetan);#Computing sine term


		g = g + np.abs(Hn)*an*cost + np.abs(Hn)*bn*sint; #evaluating the summation


plt.plot(t,g)
plt.grid ()
plt.xlabel('$t$')
plt.ylabel('$g(t)$')
#Save figure, remove the following line while running the program
plt.savefig('../figs/2.5.eps')
plt.show()








