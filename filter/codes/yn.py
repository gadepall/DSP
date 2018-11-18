import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex

n=np.linspace(-2,3,6)
x=np.array([1,2,3,4,2,1])

k = 10
y = np.zeros((n,1))
y[0] = x[0]
y[1] = x[1] - 0.5*y[0]
for n in range(2,10):
	 y[n] =- 0.5*y[n-1] + x[n] + x[n-2]
end


plt.stem(n,x)
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
#If using termux
plt.savefig('../figs/xn.pdf')
plt.savefig('../figs/xn.eps')
subprocess.run(shlex.split("termux-open ../figs/xn.pdf"))
#else
plt.show()
