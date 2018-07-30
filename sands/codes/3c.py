import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import shift


n=np.linspace(-3,7,11)
#x(n)
xn=np.array([0,0,0,0,2,3,1,0,0,0,0])
#x(n-2)
xn_right=shift(xn, 2, cval=0)

plt.stem(n,xn_right)
plt.xlabel('$n$')
plt.ylabel('$x(n-2)$')
plt.ylim((0,4))
#Ignore the following command
plt.savefig('../figs/3c.eps')
plt.show()
