import numpy as np
import matplotlib.pyplot as plt

n=np.linspace(-3,7,11)
x=np.array([0,0,0,0,2,3,1,0,0,0,0])
plt.stem(n,x)
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.ylim((0,3))
#Ignore the following command
plt.savefig('../figs/3a.eps')
plt.show()
