import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
b = 0.05
m = 0.01
l = 0.5
g = 9.8
def model(u,t):
    return[u[1],(-b/m)*u[1]-(g/l)*np.sin(u[0])]
x = [0,3]
t = np.linspace(0,5)
us = odeint(model,x,t)
xs = us[:,0]
plt.plot(t,xs)
plt.show()
