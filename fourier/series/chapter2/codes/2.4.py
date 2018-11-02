import numpy as np

#Filter Characteristics

R = 1e3; #1K ohm resistance
C = 10e-6;#10 uF capacitance


#finding 3 dB bandwidth theoretically

q = -31/3;
r = -1015/27;

print(np.sqrt((-r/2 + np.sqrt(r**2/4 +q**3/27))**(1/3) + (-r/2 - np.sqrt(r**2/4 +q**3/27))**(1/3) - 13/3)/(2*np.pi*R*C))




