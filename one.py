import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,4*np.pi,1000)
x = np.cos(t)*np.cos(5*t) + np.cos(5*t)

fig, a = plt.subplots(2,1)
a[0].plot(t,x)
a[0].set_title("plot")
a[1].hist(x,bins=[1,2,3,4,5])
a[1].set_title('histogram')
fig.tight_layout()
plt.show()
