import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Определение параметров поверхности
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)

# Параметрическое задание поверхности

# Параметрическое задание поверхности
x_surface = np.outer(phi, np.cos(theta))
y_surface = np.outer(phi, np.sin(theta))
z_surface = np.outer(np.ones(np.size(theta)), theta * 0.1)

ax.plot_surface(x_surface, y_surface, z_surface)

plt.savefig('test.png')