import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#Wave Amplitude
A=5
#Wave Period
T = 0.02;
#Time Samples
t = np.linspace(-2.5*T,2.5*T,1e4)
#Plot wave
plt.plot(t, A/2*(1+signal.square(2*np.pi*t/T)))
plt.ylim(-1, 6)
plt.grid()
plt.xlabel('$t$')
plt.ylabel('$g(t)$')
#Save figure
plt.savefig('../figs/1.1.eps')
plt.show()



