import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

t1=np.linspace(-3,0,100)
t2=np.linspace(0,2,100)
t3=np.linspace(2,4,100)

x1=0*np.ones(100)
x2=t2**2
x=np.concatenate((x1,x2,x1),axis=0)
t=np.concatenate((t1,t2,t3),axis=0)

E,err=integrate.quad(lambda t: t**4,0.,2.)
print (E)

plt.plot(t,x)
plt.grid()
plt.xlabel('$t$')
plt.ylabel('x(t)$')
plt.show()
