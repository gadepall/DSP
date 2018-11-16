import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import shift

#x(n-2)
x=[-1,-1,-1,1,-1,1,1,1]
#h(n)
h=[0,-1,1]
#y(n-2)
yns=np.convolve(x,h)
n = np.linspace(-2,7,10)
plt.stem(n,yns)
#plt.stem(yns)
plt.xlabel('n')
plt.ylabel('y(n)=x(n)*h(n)')
plt.grid()

plt.show()
