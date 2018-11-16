import numpy as np
import matplotlib.pyplot as plt

#|t| < 1
t1=np.linspace(-1,1,25)
x1=2+abs(t1)

#1 < |t| < 4 
t2=np.linspace(1,4,25)
x2=-abs(t2)+4
t3=np.linspace(-4,-1,25)
x3=(t3)+4

#x(t)
x=np.concatenate((x3,x1,x2), axis = 0)

t = np.concatenate((t3,t1,t2), axis = 0)

#x(-t)
xflip = np.fliplr([x])[0]


#Plotting
plt.plot(t,x, label='$x(t)$')
plt.plot(t,xflip,'o', mfc='none', label='$x(-t)$')

plt.grid()
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.legend()
##Ignore the following command
plt.savefig('../figs/4a.eps')
plt.show()
