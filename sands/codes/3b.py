import numpy as np
import matplotlib.pyplot as plt

n=np.linspace(-3,7,11)
x=np.array([0,0,0,0,2,3,1,0,0,0,0])
plt.stem(n,3*x)
plt.xlabel('$n$')
plt.ylabel('$3x(n)$')
plt.ylim((0,10))
#Ignore the following command
plt.savefig('../figs/3b.eps')
plt.show()
