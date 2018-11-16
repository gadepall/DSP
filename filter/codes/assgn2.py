import numpy as np
import matplotlib.pyplot as plt

def is_periodic(samples, value, tolerance=0):
    diffs = [a-b for a, b in zip(samples, samples[1:])]
    return all(d-tolerance <= value <= d+tolerance for d in diffs)


n=np.linspace(-3,7,11)
x=np.array([0,0,0,0,2,3,1,0,0,0,0])
x1=3*x
Shift1=2;
Shift2=3;

#print x1
#print x2

plt.figure(1)
plt.stem(n,x)
plt.xlabel('$n$')
plt.ylabel('$x[n]$')

plt.figure(2)
plt.stem(n,x1)
plt.xlabel('$n$')
plt.ylabel('$3*x[n]$')

plt.figure(3)
plt.stem(n+Shift1,x)
plt.xlabel('$n$')
plt.ylabel('$x[n-2]$')

plt.figure(4)
plt.stem(Shift2-n,x)
plt.xlabel('$n$')
plt.ylabel('$x[3-n]$')

E=0
for i in range (-3,6):
    E+=(x[i]**2)


print ('x[n] is eneregy signal')
print (E)

C=0
for i in range (-3,0):
    if x[i]==0:
        C=C+1
if C==3:
    print ('x[n] is causal')

p=0
for i in range(1,10):
    X=is_periodic(x,i,1)
    if X==True:
        print ('x(t) is periodic')
        p=p+1

if (X==False and p==0):
    print ('x(t) is aperiodic signal')

plt.show()
