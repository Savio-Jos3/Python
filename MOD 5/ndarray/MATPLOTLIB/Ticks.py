import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Function")

# Set custom x and y ticks
plt.xticks(
    [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],  # positions
    ['0', 'π/2', 'π', '3π/2', '2π']            # labels
)
plt.yticks([-1, 0, 1])

plt.grid(True)
plt.show()
