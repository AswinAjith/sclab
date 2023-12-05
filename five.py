import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,0.002,0.00002)
f = 1000
y = 2 + np.sin(2*np.pi*f*t)
data = np.column_stack((t,y))
plt.plot(t,y)
plt.show()
np.savetxt('waveform.csv',data,delimiter=',',header="Sampling Time, Sample",comments = '')
