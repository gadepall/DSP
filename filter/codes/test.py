from pydub import AudioSegment
#from struct import *
from scipy.io import wavfile
from scipy.stats import norm
import scipy
import matplotlib.pyplot as plt
import numpy as np


#sound = AudioSegment.from_mp3("aud1.mp3")
#sound.export("test.wav", format="wav")

#fs, data=wavfile.read('test.wav')
#D=data*1.0/(2**15)
#d=D[:,0]

#rv=np.round(d)
#plt.figure(1)
##plt.plot(d)
#plt.stem(d)
#plt.xlabel('n')
#plt.ylabel('x[n]')
#plt.grid()

#x=[]
#for i in range (3000,4000):
    #x.append(d[i])

#plt.stem(x)
#plt.xlabel('n')
#plt.ylabel('x[n] for 3000<n<4000')
#plt.show()

fs, data=wavfile.read('aud1.wav')
D=data*1.0/(2**15)
d=D[:,0]

rdata=[]
for i in range (0,1652600):
    rdata.append([data[i+1][0],data[i+1][0]])

data2 = np.asarray(rdata, dtype=np.int16)
wavfile.write('outout.wav',fs,data2)
#decimation 
