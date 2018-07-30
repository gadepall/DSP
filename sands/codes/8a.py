import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import shift

t1=np.linspace(-6,-4,40)
t2=np.linspace(-4,-2,40)
t3=np.linspace(-2,2,80)
t4=np.linspace(2,4,40)
t5=np.linspace(4,6,40)

x2=t2+4
x3=t3*0
x4=t4-4
x1=t1*0

x=np.concatenate((x1,x2,x3,x4,x1),axis=0)

t=np.concatenate((t1,t2,t3,t4,t5),axis=0)

# 0-1 x(t) has 10 samples i.e., x(t+1)=x(n-20)
andig = 20
anshift = -1

x_t=shift(x,anshift*andig,cval=0)

plt.plot(t,x,label='x(t)')
plt.plot(t,x_t,label='x(t+1)')
plt.xlabel('t')
plt.ylabel('$x(t)$ and $x(t+1)$')
plt.axis([-6,6,-3,3])
plt.grid()
plt.legend()
#Ignore the following command
plt.savefig('../figs/8a.eps')
plt.show()
