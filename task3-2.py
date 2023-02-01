import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_cone(ax):
    """
    Plots the HSV cone in the given axis.
    """
    theta = np.linspace(0, 2 * np.pi, 100)
    y = np.linspace(0, 1, 100)
    theta_grid, y_grid = np.meshgrid(theta, y)
    x_grid = y_grid * np.cos(theta_grid)
    z_grid = y_grid * np.sin(theta_grid)

    ax.plot_surface(x_grid, y_grid, z_grid, cmap='hsv')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot_cone(ax)
ax.set_xlabel('Hue')
ax.set_ylabel('Saturation')
ax.set_zlabel('Value')
plt.show()
