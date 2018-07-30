import numpy as np
import matplotlib.pyplot as plt

#-4 < t <-1
t3=np.linspace(-4,-1,60)
x3=t3+4

#-1 < t < 0 
t1=np.linspace(-1,0,20)
x1=-5*t1-2

#0 < t < 3 
t2=np.linspace(0,3,60)
x2=(2.0/3)*(t2-3)

#3 < t <4
t4=np.linspace(3,4,20)
z=np.zeros(20)

#x(t)
x=np.concatenate((x3,x1,x2,z), axis = 0)

t = np.concatenate((t3,t1,t2,t4), axis = 0)

#x(-t)
xflip = np.fliplr([x])[0]

#Plotting
plt.plot(t,x, label='$x(t)$')
plt.plot(t,xflip, label='$x(-t)$')

plt.grid()
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.legend()
plt.axis('equal')
##Ignore the following command
plt.savefig('../figs/4b.eps')
plt.show()
