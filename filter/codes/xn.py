import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex

n=np.linspace(-2,3,6)
x=np.array([1,2,3,4,2,1])
plt.stem(n,x)
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
#If using termux
plt.savefig('../figs/xn.pdf')
plt.savefig('../figs/xn.eps')
subprocess.run(shlex.split("termux-open ../figs/xn.pdf"))
#else
plt.show()
