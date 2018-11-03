import numpy as np
#Filter Characteristics
R = 1e3; #1K ohm resistance
C = 10e-6;#10 uF capacitance

#finding 3 dB bandwidth numerically
print(np.sqrt(np.roots([1,  13,  46,  -1]))/(2*np.pi*R*C))



