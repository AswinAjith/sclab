import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1.3*np.pi,100)
v = np.sin(3*t)
v[v<0] = 0
fig, a = plt.subplots(2,1)
a[0].plot(t,v)
plt.show()
a[1].hist(v,bins=5)
plt.show()
