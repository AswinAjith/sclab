import numpy as np
from matplotlib import pyplot as plt

t = np.arange(0,0.003,0.00003)
f = 1000
y = 2+5*np.sin(2*np.pi*f*t)
plt.plot(t,y)
np.savetxt('waveform2.csv',y,delimiter=',')

y = np.genfromtxt('waveform2.csv',delimiter = ',')
fig, a = plt.subplots(2,1)
a[0].plot(y)
a[0].set_title('waveform')
a[1].hist(y,bins = [-5,-4,-3,-2,-1,0,1,2,3,5,6,7,8])
a[1].set_title('Histogram')
fig.tight_layout()
plt.show()
