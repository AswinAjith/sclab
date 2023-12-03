import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,4*np.pi,100)

f1 = np.sin(t)
f2 = np.cos(t)

fig, a = plt.subplots(3,1)

a[0].scatter(t,f1,color='g',marker='o')
a[0].set_title('scatter plot')
a[1].scatter(t,f2,color='b',marker='o')
a[1].set_title('scatter plot cos(t)')
a[2].scatter(f1,f2,color='r',marker = 'x')
fig.tight_layout()
plt.show()
