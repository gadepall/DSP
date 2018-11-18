import numpy as np
import matplotlib.pyplot as plt
#comment the following 2 lines
import subprocess
import shlex

def H(f):
	s = 1j*2*np.pi*f
	den = np.polyval([1,1],s*C*R)
	H = 1/den
	return H
		

#Filter Characteristics
R = 5*1e2; #500 ohm resistance
C = 10e-6;#10 uF capacitance

#Input and Output
f_0 = 50.0
t = np.linspace(-50e-3,50e-3,5e2)
xt = np.cos(2*np.pi*f_0*t)
yt = abs(H(f_0))*np.cos(2*np.pi*f_0*t + np.angle(H(f_0)))

#subplots
plt.subplot(2, 1, 1)
plt.plot(t, xt)
plt.title('Sinusoidal Response')
plt.ylabel('$x(t)$')
plt.grid()# minor


plt.subplot(2, 1, 2)
plt.plot(t, yt)
plt.xlabel(' t (ms)')
plt.ylabel('$y(t)$')
plt.grid()# minor

#Save figure. Comment the following two lines
plt.savefig('../figs/xtyt.pdf')
subprocess.run(shlex.split("termux-open ../figs/xtyt.pdf"))
#uncomment this line
#plt.show()





