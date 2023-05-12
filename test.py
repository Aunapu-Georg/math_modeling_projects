import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
 
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
 
N = 20
edge = 20
step = 5
phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, np.pi, 100)
 
def animate(delta):
    x = np.outer(phi, np.cos(theta)) + np.outer(np.ones(np.size(theta)) * delta, np.ones(np.size(theta)))
    y = np.outer(phi, np.sin(theta))
    z = np.outer(np.ones(np.size(theta)), theta * step)
    return x, y, z
 
for i in range(N):
 
    coordinates = animate(0.5 * i)
    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]
    ax.plot_surface(x, y, z, color='b')
    plt.savefig(f'pic_{i}')

ax.set_xlim3d([-edge, edge])
ax.set_xlabel('X')

ax.set_ylim3d([-edge, edge])
ax.set_ylabel('Y')

ax.set_zlim3d([-edge, edge])
ax.set_zlabel('Z')

# Создание анимации из отдельных кадров
images = []
filenames = [f'pic_{i}.png' for i in range(N)]
for filename in filenames:
    images.append(imageio.imread(filename))
    os.remove(filename)
imageio.mimsave('test.gif', images)
