import matplotlib.pyplot as plt
import numpy as np
import math

#Create a sinwave

x=np.arange(0,math.pi*2,0.15)
y=np.sin(x)
plt.plot(x,y)
plt.title("Sinwave")
plt.xlabel("Angle")
plt.ylabel("Sin")
plt.show()
