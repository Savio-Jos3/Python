import matplotlib.pyplot as plt
import numpy as np
import math

# Define the x range
x = np.arange(-2 * math.pi, 2 * math.pi, 0.005)

# Plot sin(x)
plt.plot(x, np.sin(x), label='sin')

# Plot cos(x)
plt.plot(x, np.cos(x), label='cos', color='red', linestyle='--', marker='o', markevery=200)

# Plot -sin(x) with a valid linestyle and marker
plt.plot(x, -np.sin(x), label='-sin', color='green', linestyle='-.', marker='x', markevery=200)

# Labels and title
plt.title('Sin and Cos')
plt.xlabel('Angle')
plt.ylabel('Sin and Cos')

# Legend and grid
plt.legend(loc='upper right')
plt.grid()

# Show plot
plt.show()
