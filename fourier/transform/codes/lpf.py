import numpy as np
import matplotlib.pyplot as plt

#Filter Characteristics

R = 5*1e2; #1K ohm resistance
C = 10e-6;#10 uF capacitance

#Plotting the filter amplitude response
f_0 = 50
f = np.linspace(-3*f_0,3*f_0,1e2)
s = 1j*2*np.pi*f

den = np.polyval([1,1],s*C*R);
H = 1/den;

plt.plot(f,abs(H))
plt.grid()# minor
plt.xlabel('$f$ (Hz)')
plt.ylabel('$H(f)$')
#Save figure
#plt.savefig('../figs/lpf.eps')
plt.show()





