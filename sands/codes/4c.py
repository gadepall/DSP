import numpy as np
import matplotlib.pyplot as plt

#-4 < t < -3
t7=np.linspace(-4,-3,25)
x7=(t7+4)*3

#-3 < t < -2
t5=np.linspace(-3,-2,25)
x5=(-5*t5)-12

# -2 < t < -1
t4=np.linspace(-2,-1,25)
x4=3*(t4)+4

#-1 < t < 1
t1=np.linspace(-1,1,25)
x1=-t1

#1 < t < 2
t2=np.linspace(1,2,25)
x2=3*(t2)-4

#2 < t < 3
t3=np.linspace(2,3,25)
x3=(-5*t3)+12

#3 < t < 4
t6=np.linspace(3,4,25)
x6=(t6-4)*3

#x(t)
x=np.concatenate((x7,x5,x4,x1,x2,x3,x6), axis = 0)

t = np.concatenate((t7,t5,t4,t1,t2,t3,t6), axis = 0)

#x(-t)
xflip =np.fliplr([x])[0]

#Plotting
plt.plot(t,x, label='$x(t)$')
plt.plot(t,xflip,'o', mfc='none', label='$x(-t)$')

plt.grid()
plt.xlabel('$t$')
plt.ylabel('$x(t)$ and $x(-t)$')
plt.legend()
##Ignore the following command
plt.savefig('../figs/4c.eps')
plt.show()
