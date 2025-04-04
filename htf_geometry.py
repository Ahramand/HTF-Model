# htf_geometry.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Golden Ratio
phi = (1 + np.sqrt(5)) / 2

# Parameters
R, r = 3.0, 1.0           # Major/minor radius
alpha, beta = 0.3, 0.3    # Helix amplitudes
theta = np.linspace(0, 2 * np.pi, 100)
t = np.linspace(0, 4 * np.pi, 200)
Theta, T = np.meshgrid(theta, t)

# Parametric equations for Helical Torus
X = (R + r * np.cos(T)) * np.cos(Theta) + alpha * np.sin(phi * T)
Y = (R + r * np.cos(T)) * np.sin(Theta) + alpha * np.cos(phi * T)
Z = r * np.sin(T) + beta * np.sin(phi * T)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)
ax.set_title("Helical Torus Flux Geometry")
plt.tight_layout()
plt.show()
