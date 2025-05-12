import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-2 * math.pi, 2 * math.pi, 0.005)

# Set up a figure with 3 vertically stacked subplots
plt.figure(figsize=(10, 8))

# Subplot 1: sin(x)
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x), label='sin', color='blue')
plt.title('sin(x)')
plt.xlabel('Angle')
plt.ylabel('Sin')   
plt.grid()
plt.legend()

# Subplot 2: cos(x)
plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x), label='cos', color='red', linestyle='--', marker='o', markevery=200)
plt.title('cos(x)')
plt.xlabel('Angle')
plt.ylabel('Cos')
plt.grid()
plt.legend()

# Subplot 3: -sin(x)
plt.subplot(2, 2, 3)
plt.plot(x, -np.sin(x), label='-sin', color='green', linestyle='-.', marker='x', markevery=200)
plt.title('-sin(x)')
plt.xlabel('Angle')
plt.ylabel('-Sin')
plt.grid()
plt.legend()

# Subplot 4: sin(x) and cos(x) together
plt.subplot(2, 2, 4)
plt.plot(x, np.sin(x), label='sin', color='blue')
plt.plot(x, np.cos(x), label='cos', color='red', linestyle='--', marker='o', markevery=200) 
plt.title('sin(x) and cos(x)')
plt.xlabel('Angle')
plt.ylabel('Sin and Cos')
plt.grid()
plt.legend()

# Adjust layout
plt.tight_layout()
plt.show()
