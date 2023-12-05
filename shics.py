import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def rl_circuit(y,t):
    r_over_l = 1
    dydt = (-r_over_l)*y + 5*np.exp(-t)
    return dydt

y0 = 0

t = np.linspace(0,10,1000)

solution = odeint(rl_circuit,y0,t)

plt.plot(t,solution,label='Current (A)')
plt.xlabel('Time')
plt.ylabel('Current')
plt.legend()
plt.grid(True)
plt.show()
