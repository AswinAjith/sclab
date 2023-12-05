#8
import numpy as np
import matplotlib.pyplot as plt
import math
t=100
sum=5
arr=[]
for i in range(1,100):
  y=((40*np.cos((math.pi)/10))*t)/(((2*i-1)*np.pi)**2)
  sum=sum+y
  arr.append(y)
plt.plot(arr)
plt.show()
