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

# 0-1 x(t) has 20 samples i.e., x(t-1)=x(t-20)
andig = 20
#2x(t-2)
anshift = 2
x_t=shift(2*x,anshift*andig,cval=0)

plt.plot(t,x,label='x(t)')
plt.plot(t,x_t,label='2x(t-2)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.legend()
#Ignore the following command
plt.savefig('../figs/8b.eps')
plt.show()
