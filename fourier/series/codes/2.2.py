import numpy as np
import matplotlib.pyplot as plt



#Filter Characteristics

R = 1e3; #10K ohm resistance
C = 10e-6;#10 uF capacitance

#Plotting the filter amplitude response
T = 0.02;
f_0 = 1/T;
f = np.linspace(-1.5*f_0,1.5*f_0,1e2)
s = 1j*2*np.pi*f

den = np.polyval([1,-5, 6, 1],s*C*R);
H = 1/den;

plt.plot(f,abs(H))
plt.grid()# minor
plt.xlabel('$f$ (Hz)')
plt.ylabel('$H(f)$')
#Save figure
plt.savefig('../figs/2.2.eps')
plt.show()





