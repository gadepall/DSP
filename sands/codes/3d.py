import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import shift


#x(n)
xn=np.array([0,0,0,0,2,3,1])
#x(-n)
xflip = np.flip(xn,0)
#x(3-n)
xflip_right=shift(xflip, 3, cval=0)
#plotting
n=np.linspace(-3,3,7)
plt.stem(n,xflip_right)
plt.xlabel('$n$')
plt.ylabel('$x(3-n)$')
plt.ylim((0,4))
##Ignore the following command
plt.savefig('../figs/3d.eps')
plt.show()
