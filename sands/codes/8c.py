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
#x(-t)
x_t=np.fliplr([x])[0]

y=x-x_t
plt.plot(t,x,label='x(t)')
plt.plot(t,y,label='x(t)-x(-t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.axis('equal')
plt.grid()
plt.legend()
plt.show()

