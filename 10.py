import numpy as np
import matplotlib.pyplot as plt
time = np.linspace(-10,10,100)
sinc_values = np.sinc(time)
fig, a = plt.subplots(2,1)
a[0].plot(time,sinc_values)
a[0].set_title("sinc functions")
a[1].hist(time,bins=[-10,0,10])
a[1].set_title("Histrogram")
plt.show()
